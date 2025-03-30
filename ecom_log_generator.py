import random
import json
import time
from datetime import datetime
import uuid
import os

class EcomLogGenerator:
    def __init__(self):
        self.users = [f"user_{i}" for i in range(1, 101)]
        self.products = ["T-shirt", "Jeans", "Shoes", "Watch", "Phone", "Laptop"]
        self.statuses = ["success", "failed", "pending"]
        self.log_file = os.environ.get('LOG_FILE', '/var/log/ecom_logs.log')

    def generate_base_event(self):
        return {
            "timestamp": datetime.now().isoformat(),
            "request_id": str(uuid.uuid4()),
            "user_id": random.choice(self.users),
            "service": "ecom-api"
        }

    def generate_signup(self):
        event = self.generate_base_event()
        event.update({
            "operation": "signup",
            "status": random.choice(self.statuses),
            "duration_ms": random.randint(100, 1000),
            "email": f"{event['user_id']}@example.com"
        })
        return event

    def generate_order(self):
        event = self.generate_base_event()
        status = random.choice(self.statuses)
        event.update({
            "operation": "order",
            "status": status,
            "duration_ms": random.randint(200, 2000),
            "order_id": str(uuid.uuid4()),
            "items": [{
                "product": random.choice(self.products),
                "quantity": random.randint(1, 5),
                "price": round(random.uniform(10.0, 199.99), 2)
            } for _ in range(random.randint(1, 3))],
            "total": round(random.uniform(10.0, 500.0), 2)
        })
        if status == "failed":
            event["error"] = random.choice([
                "Payment declined",
                "Inventory insufficient",
                "Timeout error"
            ])
        return event

    def generate_login(self):
        event = self.generate_base_event()
        event.update({
            "operation": "login",
            "status": random.choice(self.statuses),
            "duration_ms": random.randint(50, 500)
        })
        return event

    def generate_cart_action(self):
        event = self.generate_base_event()
        event.update({
            "operation": "cart",
            "action": random.choice(["add", "remove", "update"]),
            "status": random.choice(self.statuses),
            "duration_ms": random.randint(50, 300),
            "product": random.choice(self.products),
            "quantity": random.randint(1, 5)
        })
        return event

    def write_log(self, event):
        with open(self.log_file, 'a') as f:
            f.write(json.dumps(event) + '\n')

    def run(self):
        event_types = [
            self.generate_signup,
            self.generate_order,
            self.generate_login,
            self.generate_cart_action
        ]
        
        while True:  # Run indefinitely for container
            event = random.choice(event_types)()
            self.write_log(event)
            print(json.dumps(event))  # Also print to stdout for CloudWatch
            time.sleep(random.uniform(0.1, 2.0))

if __name__ == "__main__":
    generator = EcomLogGenerator()
    generator.run()
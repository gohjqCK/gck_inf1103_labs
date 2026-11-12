from Modules.Orderline import Orderline
from Modules.Product import Product

class Order:
    def __init__(self, order_id: str):
        self.order_id: str = order_id
        self.order_lines: list[Orderline] = []

    def add_order_line(self, product: Product, quantity: int) -> None:
        order_line = Orderline(product, quantity)
        self.order_lines.append(order_line)

    def remove_order_line(self, product_id):
        for line in self.order_lines:
            if line.product.product_id == product_id:
                self.order_lines.remove(line)
                return "success"
        return "fail"

    def view_order(self):
        for order in self.order_lines:
            print(f"Order ID: {self.order_id}")
            print(f"{order.product.name} (ID: {order.product.product_id}) | "
              f"Qty: {order.quantity} | Subtotal: ${order.calculate_subtotal():.2f}")
        print(f"Total: ${self.calculate_total():.2f}\n")

    def calculate_total(self) -> float:
        total = 0.0
        for order_line in self.order_lines:
            total += order_line.calculate_subtotal()
        return total
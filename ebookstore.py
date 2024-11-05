# E-bookstore Management System Classes
# Author: Student
# Date of creation: 11-04-2024

class EBook:
    """Class for EBooks in the E-bookstore."""

    def __init__(self, title, author, genre, price, publication_date):
        # Initialize EBook attributes with provided values
        self.__title = title
        self.__author = author
        self.__genre = genre
        self.__price = price
        self.__publication_date = publication_date

    def __str__(self):
        # Return a formatted string representation of the EBook
        return "Title: {}, Author: {}, Genre: {}, Price: ${}, Publication Date: {}".format(
            self.__title, self.__author, self.__genre, self.__price, self.__publication_date)


class Discount:
    """Class for Discounts with different types."""

    def __init__(self, discount_type, discount_amount=0.0):
        # Initialize discount type and amount
        self.__discount_type = discount_type
        self.__discount_amount = discount_amount

    def calculate_discount(self, total_price):
        """Calculate discount based on total price."""
        # Calculate the discount amount on the given total price
        return total_price * (self.__discount_amount / 100)

    def __str__(self):
        # Return a formatted string representation of the discount
        return "Discount Type: {}, Amount: {}%".format(self.__discount_type, self.__discount_amount)


class ShoppingCart:
    """Class for ShoppingCart that holds EBooks."""

    def __init__(self):
        # Initialize an empty list of EBooks and total price
        self.__ebooks = []  # List of EBook objects (Composition relationship with EBook)
        self.__total_price = 0.0

    def add_ebook(self, ebook):
        # Add an EBook to the cart and update the total price
        self.__ebooks.append(ebook)
        self.calculate_total()

    def remove_ebook(self, ebook):
        # Remove an EBook from the cart and update the total price
        if ebook in self.__ebooks:
            self.__ebooks.remove(ebook)
            self.calculate_total()

    def calculate_total(self):
        # Calculate the total price of all EBooks in the cart
        self.__total_price = sum(ebook._EBook__price for ebook in self.__ebooks)

    def __str__(self):
        # Return a formatted string representation of the ShoppingCart
        ebooks_str = ", ".join(str(ebook) for ebook in self.__ebooks)
        return " Shopping Cart Total: ${}, EBooks: [{}]".format(self.__total_price, ebooks_str)


class Customer:
    """Base class for all customers."""

    def __init__(self, name, email):
        # Initialize customer name and email
        self.name = name
        self.email = email

    def get_discount(self):
        """Returns the discount percentage for the customer."""
        # Default discount is 0% for regular customers
        return 0

    def __str__(self):
        # Return a formatted string representation of the Customer
        return "Customer Name: {}, Email: {}, Discount: {}%".format(self.name, self.email, self.get_discount())


class RegularCustomer(Customer):
    """Class for regular customers without additional discounts."""

    def __init__(self, name, email):
        # Inherit name and email from the Customer superclass (Inheritance relationship)
        super().__init__(name, email)


class LoyaltyCustomer(Customer):
    """Class for loyalty program members who receive an automatic discount."""

    def __init__(self, name, email, loyalty_discount=10):
        # Initialize loyalty customer with a discount percentage
        super().__init__(name, email)  # Inheritance relationship with Customer
        self.loyalty_discount = loyalty_discount

    def get_discount(self):
        """Overrides the base discount method to return the loyalty discount."""
        # Return the loyalty discount for this customer
        return self.loyalty_discount

    def __str__(self):
        # Return a formatted string with loyalty membership status
        return "{} (Loyalty Member)".format(super().__str__())


class Order:
    """Class for Orders linking Customer, ShoppingCart, and Discounts."""

    def __init__(self, customer, cart):
        # Initialize order with customer, cart, discounts, and invoice
        self.__customer = customer  # Aggregation relationship with Customer
        self.__cart = cart  # Aggregation relationship with ShoppingCart
        self.__discounts = []  # List of Discount objects (Aggregation relationship)
        self.__invoice = None  # Invoice generated after order placement

    def add_discount(self, discount):
        # Add a discount to the order
        self.__discounts.append(discount)

    def apply_discounts(self):
        # Calculate total price after applying customer-specific and additional discounts
        total_price = self.__cart._ShoppingCart__total_price
        total_price -= total_price * (self.__customer.get_discount() / 100)
        for discount in self.__discounts:
            total_price -= discount.calculate_discount(total_price)
        return total_price

    def generate_invoice(self):
        # Generate an invoice for the order with discounted price and tax
        final_amount = self.apply_discounts()
        tax = final_amount * 0.08  # Example VAT rate of 8%
        self.__invoice = Invoice(self.__cart._ShoppingCart__ebooks, self.__cart._ShoppingCart__total_price,
                                 final_amount, tax)
        return self.__invoice

    def __str__(self):
        # Return a formatted string representation of the Order
        discounts_str = ", ".join(str(discount) for discount in self.__discounts)
        return " Order for: {}, Cart: {}, Discounts: [{}]".format(self.__customer, self.__cart, discounts_str)


class Invoice:
    """Class for Invoices detailing the final purchase details."""

    def __init__(self, items, total_amount, discounted_total, tax):
        # Initialize invoice with items, total amount, discounted total, and tax
        self.__items = items  # Composition relationship with EBooks
        self.__total_amount = total_amount
        self.__discounted_total = discounted_total
        self.__tax = tax
        self.__final_total = discounted_total + tax

    def __str__(self):
        # Return a formatted string representation of the Invoice
        items_str = ", ".join(str(item) for item in self.__items)
        return " Items: [{}], Total Amount: ${}, Discounted Total: ${}, Tax: ${}, Final Total: ${}".format(
            items_str, self.__total_amount, self.__discounted_total, self.__tax, self.__final_total)


class CustomerManager:
    """Class to manage customer accounts in the e-bookstore."""

    def __init__(self):
        # Initialize an empty list of customers
        self.customers = []  # List to hold Customer objects (Aggregation relationship)

    def add_customer(self, customer):
        """Add a new customer account."""
        # Add a customer to the list and print confirmation
        self.customers.append(customer)
        print("Customer '{}' added successfully.".format(customer.name))

    def remove_customer(self, email):
        """Remove an existing customer account by email."""
        # Find and remove customer by email, print confirmation if found
        for customer in self.customers:
            if customer.email == email:
                self.customers.remove(customer)
                print("Customer '{}' removed successfully.".format(customer.name))
                return
        print("Customer not found.")

    def modify_customer(self, email, name=None, new_email=None):
        """Modify an existing customer account."""
        # Modify customer details based on email, print confirmation if found
        for customer in self.customers:
            if customer.email == email:
                if name:
                    customer.name = name
                if new_email:
                    customer.email = new_email
                print("Customer '{}' modified successfully.".format(email))
                return
        print("Customer not found.")

    def list_customers(self):
        """List all customer accounts."""
        # Print all customer details or notify if no customers available
        if not self.customers:
            print("No customers available.")
        for customer in self.customers:
            print(customer)

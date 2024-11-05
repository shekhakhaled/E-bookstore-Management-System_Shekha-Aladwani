from ebookstore import EBook, RegularCustomer, LoyaltyCustomer, ShoppingCart, Order, Invoice, CustomerManager

# 1. Adding a list of e-books to the catalog
# Creating multiple e-book instances
ebook1 = EBook("Where the Wild Things Are", "Maurice Sendak", "Picture Book", 8.99, "November 13, 1963")
ebook2 = EBook("Charlotte's Web", "E.B. White", "Children's Literature", 7.99, "October 15, 1952")
ebook3 = EBook("Harry Potter and the Philosopher's Stone", "J.K. Rowling", "Adventure", 10.99, "June 26, 1997")
ebook4 = EBook("The Very Hungry Caterpillar", "Eric Carle", "Educational", 5.99, "June 3, 1969")
ebook5 = EBook("Goodnight Moon", "Margaret Wise Brown", "Bedtime Story", 7.99, "September 3, 1947")
ebook6 = EBook("Matilda", "Roald Dahl", "Children's Literature", 8.99, "October 1, 1988")
ebook7 = EBook("The Cat in the Hat", "Dr. Seuss", "Rhyming Story", 6.99, "March 12, 1957")
ebook8 = EBook("The Lion, the Witch and the Wardrobe", "C.S. Lewis", "Adventure", 8.99, "October 16, 1950")
ebook9 = EBook("Anne of Green Gables", "L.M. Montgomery", "Children's Literature", 9.99, "June 1908")
ebook10 = EBook("The Tale of Peter Rabbit", "Beatrix Potter", "Picture Book", 6.99, "October 1902")

# Displaying the added e-books
print("List of Books:")
print("EBook 1:", ebook1)
print("EBook 2:", ebook2)
print("EBook 3:", ebook3)
print("EBook 4:", ebook4)
print("EBook 5:", ebook5)
print("EBook 6:", ebook6)
print("EBook 7:", ebook7)
print("EBook 8:", ebook8)
print("EBook 9:", ebook9)
print("EBook 10:", ebook10)

# 2. Adding a list of customers
# Creating different types of customers
regular_customer1 = RegularCustomer("Shekha Khaled", "shekha@gmail.com")
loyalty_customer1 = LoyaltyCustomer("Hajer Mohammed", "hajer@gmail.com", loyalty_discount=10)
regular_customer2 = RegularCustomer("Raudha Fahad", "raudha@gmail.com")
loyalty_customer2 = LoyaltyCustomer("Haya Abdullah", "haya@gmail.com", loyalty_discount=10)

# Displaying the list of customers
print("\nList of Customers:")
print(" Regular Customer 1:", regular_customer1)
print(" Loyalty Customer 1:", loyalty_customer1)
print(" Regular Customer 2:", regular_customer2)
print(" Loyalty Customer 2:", loyalty_customer2)

# Actions for each customer are grouped separately below

# Actions for Loyalty Customer 1 (Hajer Mohammed)
print("\nLoyalty Customer 1 (Hajer Mohammed):")
cart_loyalty1 = ShoppingCart()
# Adding e-books to the cart to qualify for bulk discount
cart_loyalty1.add_ebook(ebook1)
cart_loyalty1.add_ebook(ebook4)
cart_loyalty1.add_ebook(ebook7)
cart_loyalty1.add_ebook(ebook8)
cart_loyalty1.add_ebook(ebook10)  # Adding 5 e-books to qualify for bulk discount
print(" Shopping Cart after adding EBook 1, EBook 4, EBook 7, EBook 8, and EBook 10:")
print(cart_loyalty1)

# Creating an order for Loyalty Customer 1 with automatic discounts
order_loyalty1 = Order(loyalty_customer1, cart_loyalty1)
print(" Order details with Loyalty and Bulk Purchase discounts applied automatically:")
print(order_loyalty1)

# Generating and displaying invoice
invoice_loyalty1 = order_loyalty1.generate_invoice()
print(" Invoice:")
print("  Price: $", invoice_loyalty1._Invoice__discounted_total)
print("  List of Items in Invoice:")
for item in invoice_loyalty1._Invoice__items:
    print("   -", item)

# Actions for Regular Customer 1 (Shekha Khaled)
print("\nRegular Customer 1 (Shekha Khaled):")
cart_regular1 = ShoppingCart()
# Adding e-books to the cart
cart_regular1.add_ebook(ebook2)
cart_regular1.add_ebook(ebook5)
cart_regular1.add_ebook(ebook8)
print(" Shopping Cart after adding EBook 2, EBook 5, and EBook 8:")
print(cart_regular1)

# Shekha removes a book from her cart
cart_regular1.remove_ebook(ebook5)
print(" Shopping Cart after removing EBook 5:")
print(cart_regular1)

# Creating an order for Regular Customer 1 (no automatic discounts, as not enough items for bulk)
order_regular1 = Order(regular_customer1, cart_regular1)
invoice_regular1 = order_regular1.generate_invoice()
print(" Invoice:")
print("  Price: $", invoice_regular1._Invoice__discounted_total)
print("  List of Items in Invoice:")
for item in invoice_regular1._Invoice__items:
    print("   -", item)

# Actions for Loyalty Customer 2 (Haya Abdullah)
print("\nLoyalty Customer 2 (Haya Abdullah):")
cart_loyalty2 = ShoppingCart()
# Adding e-books to the cart to qualify for bulk discount
cart_loyalty2.add_ebook(ebook3)
cart_loyalty2.add_ebook(ebook6)
cart_loyalty2.add_ebook(ebook9)
cart_loyalty2.add_ebook(ebook1)
cart_loyalty2.add_ebook(ebook4)  # Adding 5 e-books to qualify for bulk discount
print(" Shopping Cart after adding EBook 3, EBook 6, EBook 9, EBook 1, and EBook 4:")
print(cart_loyalty2)

# Creating an order for Loyalty Customer 2 with automatic discounts
order_loyalty2 = Order(loyalty_customer2, cart_loyalty2)
print(" Order details with Loyalty and Bulk Purchase discounts applied automatically:")
print(order_loyalty2)

# Generating and displaying invoice
invoice_loyalty2 = order_loyalty2.generate_invoice()
print(" Invoice:")
print("  Price: $", invoice_loyalty2._Invoice__discounted_total)
print("  List of Items in Invoice:")
for item in invoice_loyalty2._Invoice__items:
    print("   -", item)

# Actions for Regular Customer 2 (Raudha Fahad)
print("\nRegular Customer 2 (Raudha Fahad):")
cart_regular2 = ShoppingCart()
# Adding e-books to the cart
cart_regular2.add_ebook(ebook1)
cart_regular2.add_ebook(ebook4)
cart_regular2.add_ebook(ebook10)
print(" Shopping Cart after adding EBook 1, EBook 4, and EBook 10:")
print(cart_regular2)

# Raudha adds another book to her cart
cart_regular2.add_ebook(ebook5)
print(" Shopping Cart after adding another book (EBook 5):")
print(cart_regular2)

# Creating an order for Regular Customer 2 (no automatic discounts, as not enough items for bulk)
order_regular2 = Order(regular_customer2, cart_regular2)
invoice_regular2 = order_regular2.generate_invoice()
print(" Invoice:")
print("  Price: $", invoice_regular2._Invoice__discounted_total)
print("  List of Items in Invoice:")
for item in invoice_regular2._Invoice__items:
    print("   -", item)

# Customer Account Management with CustomerManager
# Instantiate the CustomerManager
customer_manager = CustomerManager()

# Adding customers to the CustomerManager
print("\nAdding Customers to CustomerManager:")
customer_manager.add_customer(regular_customer1)
customer_manager.add_customer(loyalty_customer1)
customer_manager.add_customer(regular_customer2)
customer_manager.add_customer(loyalty_customer2)

# Displaying all customers
print("\nList of Customers in CustomerManager after Adding:")
customer_manager.list_customers()

# Modifying a customer
print("\nModifying Customer 'shekha@gmail.com' in CustomerManager:")
customer_manager.modify_customer("shekha@gmail.com", name="Shekha K. Updated", new_email="shekha_k@gmail.com")

# Displaying all customers after modification
print("\nList of Customers in CustomerManager after Modification:")
customer_manager.list_customers()

# Removing a customer
print("\nRemoving Customer 'hajer@gmail.com' from CustomerManager:")
customer_manager.remove_customer("hajer@gmail.com")

# Displaying all customers after removal
print("\nList of Customers in CustomerManager after Removal:")
customer_manager.list_customers()


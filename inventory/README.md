# Inventory Management Exercise

An inventory management system keeps track of products in a warehouse. The system allows adding new products, updating stock levels, and checking product availability.

## Features

The inventory management system should be able to perform the following operations:

1. **Add Product**: Add a new product to the inventory with a unique product ID, name, reorder threshold and initial stock quantity.
2. **Update Stock**: Update the stock quantity for a specific product (either adding or subtracting from the current stock).
3. **Check Stock**: Check the current stock level for a specific product.
4. **Get Stock Levels**: Retrieve a list of all products currently in the inventory, along with their stock levels.
5. **Product Availability**: Check if a specific product is available (i.e., has stock greater than zero).
6. **Reorder Products**: Automatically flag products for reorder when stock falls below a specified threshold. Retrieve all products that should be reordered.

## Conditions

### Product:

- Each product must have a unique product ID.
- Products have a stock quantity that represents the available units in the warehouse.
- A product should be flagged to reorder when the stock is equal or less than its threshold.

### Stock Updates:

- Stock can be increased or decreased, depending on inventory changes.
- Stock cannot go below zero.

### Operations:

- Adding or removing stock should update the product's stock level accordingly.
- Availability is determined based on whether the stock is greater than zero.
- The reorder flag must be removed when the stock increase above the threshold.

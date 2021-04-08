Primary key = How you would reference that particular entry 

table a = user
table b = address
table c = orders
table d = products

1 to 1:
1 entry on table a will only have a relationship to 1 entry on table b

1 to many:
1 entry on table a can have multiple entries on table c

many to many:
1 entry on table c can have multiple entries on table d and vice versa


Examples:
1 customer has 1 address = 1 to 1
1 customer has multiple orders = 1 to many
product to order = 1 to many ( many product on 1 order)
many orders containing the same type of product ( many to many)

table b and c = no relationship
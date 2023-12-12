from prettytable import PrettyTable

table = PrettyTable()

# table.field_names = ["Name", "Age", "City"]
# table.add_row(["John Doe", 30, "New York"])
# table.add_row(["Jane Doe", 25, "Los Angeles"])
table.add_column("Pokemon Name",["Pikachu","Squirtle","Charmander"])
table.add_column("Type",["Electric","Water","Fire"])

table.align = "l" #içindekileri sola yasladık

print(table)

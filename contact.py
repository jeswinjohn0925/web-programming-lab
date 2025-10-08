contacts1={
    "Anu":"9580151535",
    "Teena":"8590151535"
}
contacts2={
    "John":"9580151535",
    "Priya":"8590151535"
}
print("contact1:",contacts1)
print("contact2:",contacts2)
merged_contacts=contacts1.copy()
merged_contacts.update(contacts2)
print("Merged contacts:")
print(merged_contacts)
import pandas 

student={
    "Anu":340,
    "Teena":458,
    "John":300
}
asc_by_name=dict(sorted(student.items()))
print("sorted by Name(Ascending):",asc_by_name)


def stored(param, reverse):
    pass


desc_by_name=dict(stored(student.items(),reverse=True))
print("sorted by Name(Descending):")
print(desc_by_name)

def add_contact(args, contacts):
    name, phone = args

    if name in contacts:
        return "Contact already exists."

    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    name, phone = args

    if name not in contacts:
        return "Contact not found."

    contacts[name] = phone
    return "Contact updated."

def show_contact(name, contacts):
    if name not in contacts:
        return "Contact not found."

    return f"{name}: {contacts[name]}"

def show_all(contacts):
    if not contacts:
        return "No contacts."

    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])

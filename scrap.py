import json


def load_config(file_path='phone_list.py'):
    with open(file_path, 'r') as file:
        code = file.read()
        # Extract the phone_list dictionary
        exec(code, globals())
        return globals().get('phone_list', {})


def save_config(phone_list, file_path='phone_list.py'):
    with open(file_path, 'w') as file:
        file.write(f"phone_list = {json.dumps(phone_list, indent=4)}")


def update_phone_list(model, new_entry):
    phone_list = load_config()
    print(f'{phone_list = }')

    if 'iPhone' not in phone_list:
        phone_list['iPhone'] = {}


    phone_list['iPhone'][model] = new_entry

    save_config(phone_list)


# Example usage
new_phone_entry = [
    'https://new-link-hy.com',
    'apple iphone 18 128 gb'
]
update_phone_list('iPhone 18', new_phone_entry)
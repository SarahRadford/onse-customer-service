from behave import when


@when('I update customer "{customer_id:d}" surname to "{name}"')
def step_impl(context, customer_id, name):
    (first_name, surname) = name.split(' ', 2)
    response = context.web_client.put(
        f'/customers/{customer_id}',
        json={'firstName': first_name, 'surname': surname})

    assert response.status_code == 201, response.status_code
    context.customer_id = response.get_json()['customer_id']

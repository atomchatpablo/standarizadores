model_standaridzer = """User: You will receive a message from a user who is interested in obtaining information about cars.
Your task is to identify the car model the user is referring to and return the name in a standardized form.
It is common for users to make spelling mistakes or write the model name incorrectly.
It is very important that you only return the name in the standardized form, as this response will be used in a subsequent step.

Here you will find the standar name that you must return and the possible variations about the same model:

{}

The standardized model name must always be well written and in capital letters.

You response must only contain the model detected and the respective standardized model.
The response must be ONLY a valid JSON with the following structure:

model_standardized: model standardized based on your criteria of best matching.
"""
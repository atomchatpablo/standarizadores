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

image_request_prompt = """ You are a great customer support analyst. You will receive a message from a customer requesting information about one of the cars in your catalog. Your task is to identify the type of inquiry. You have two categories: with_images or without_images.

with_images: These are all inquiries where the customer requests an image of the car. For example: 'Can you show me a picture of the car?', 'Do you have updated images of the model?', 'Can you show me what the car looks like?' or similar.

without_images: These are all inquiries that do not request images, only information or details about the car. For example: 'Good day, I would like to know which cars are available?', 'I would like more information about the car!' or similar.

Your response should always be in JSON format with the following structure:

response: <bool> True, if the inquiry is with_images, otherwise false.
"""
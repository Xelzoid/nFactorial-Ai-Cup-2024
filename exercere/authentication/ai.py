import google.generativeai as genai

genai.configure(api_key="haha wont tell")  
model = genai.GenerativeModel('gemini-1.5-flash-latest')

def GenerateMealPlan(preferences, fitnessgoals = 'be healthy'):
    response = model.generate_content(f'''             
You are given the input text in single quotes: '{preferences}', if what is in there is not related to someone's meal preferences / requirements, 
what you respond should be should be a message that says what the user has to add/change to their message if they want to continue.
Meal preferences/requirements are like diets, allergies, dislikes, etc. 
If the input text is about or related to meal preferences / requirements, continue on with the rest of this prompt:
Check if another input text given here in single quotes: '{fitnessgoals}' is about someone's fitness goals.
Fitness goals are specific objectives individuals set to achieve desired levels of physical fitness or well-being. They can include strength/muscle gain, weight management, cardiovascular endurance, flexibility/mobility, body composition, sports performance, and overall health/well-being. 
If the second input text is not about or related to someone's fitness goals (The fitness goals do not have to be specific), what you should
output should be a message that says what the user has to add/change to their message if they want to continue.
If the second input text is actually about or related to someone's fitness goals, continue:
Someone in dire need of help achieving their fitness goals as given by the second input text needs to be given a meal plan,
you must create a 7 day meal plan that aligns with their fitness goals and accomodates anything they talked about in the first input text, 
which is their meal preferences.
Your output should be in JSON format with each day's meals listed under keys for "day1", "day2", etc. Each day should include "breakfast", "lunch", "dinner", and optionally "snacks". Ensure the meal plan is compatible with Django's JSONField.
Don't add any other text besides the meal plan json, and dont use triple quotes surrounding the json.
                                      ''')
    return response.text
def GenerateFitnessPlan(fitnessgoals):
    response = model.generate_content(f'''             
Check if this input text given here in single quotes: '{fitnessgoals}' is about someone's fitness goals.
Fitness goals are specific objectives individuals set to achieve desired levels of physical fitness or well-being. They can include strength/muscle gain, weight management, cardiovascular endurance, flexibility/mobility, body composition, sports performance, and overall health/well-being.
If the input text is not about or related to someone's fitness goals (The fitness goals do not have to be specific), output a message that says what the user has to add/change to their message if they want to continue.
If the input text is actually about or related to someone's fitness goals, continue:
Someone in dire need of help achieving their fitness goals as given by the input text needs to be given a fitness plan that describes which exercises to do, with how many sets and reps, accommodating the user's goal given by the first input text, assume the user has access to most equipment found in gyms unless told otherwise.
Output the fitness plan in JSON format. Each day should include an array of exercises, with each exercise having a name, sets, and reps. Ensure the JSON structure is clear and concise and compatible with Django's JSONField.
Dont add text besides the fitness plan json, and dont use triple quotes surrounding the json.
                                      ''')
    return response.text

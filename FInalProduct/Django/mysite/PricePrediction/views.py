from django.shortcuts import render
from django.http import JsonResponse
import pandas as pd
from django.conf import settings
import joblib

# Load MinMaxScaler object
minmax_scaler = joblib.load(settings.BASE_DIR / 'PricePrediction' / 'models' / 'minmax_scaler.pkl')

# Load LGBM model
lgbm_model = joblib.load(settings.BASE_DIR / 'PricePrediction' / 'models' / 'lgbm_model.pkl')

def homePage(request):
    if request.method == "GET":
        context = {}
        return render(request, 'home.html', context=context)

def predictionForm(request):
    if request.method == "GET":
        context = {}
        return render(request, 'predictPrice.html', context=context)
    if request.method == "POST":
        converted_values = convert_variables_to_int(request, 'list-price', 'bed-room', 'extra-space', 'wash-room', 'kitchen', 'family-room', 'community', 'garage-type', 'style')

        # Convert the dictionary to a DataFrame
        new_data = pd.DataFrame([converted_values], index=[0])

        # Predict the sold price
        final_predicted_value = scale_and_predict(new_data)


        return JsonResponse({'predicted_sold_price': final_predicted_value})
    
def scale_and_predict(unscaled_data):
    # Scale numerical features using MinMaxScaler
    scaled_user_input = minmax_scaler.transform(unscaled_data)

    final_predicted_value = lgbm_model.predict(scaled_user_input)

    return final_predicted_value[0]

def convert_variables_to_int(request, *variables):
    """
    Convert variables retrieved from a POST request to integers and derive additional values.

    Args:
    - request: Django POST request object
    - *variables: Variable names to convert

    Returns:
    - A dictionary containing variable names as keys and their corresponding integer values
    """
    converted_values = {}
    
    for variable in variables:
        # Get the value of the variable from the POST request
        value_str = request.POST.get(variable, None)
        
        if value_str is not None and value_str != '':
            try:
                converted_values[variable] = int(value_str)
            except ValueError:
                converted_values[variable] = 0
        else:
            converted_values[variable] = 0
    
    # Derive additional values based on 'family-room'
    if 'family-room' in converted_values:
        if converted_values['family-room'] == 1:
            converted_values['Family_Room_N'] = 0
            converted_values['Family_Room_Y'] = 1
        else:
            converted_values['Family_Room_N'] = 1
            converted_values['Family_Room_Y'] = 0
    
    # Remove the 'family-room' key from the dictionary
    converted_values.pop('family-room', None)
    
    # Call the map_keys_with_calculations function with the output dictionary to map with keys name as in trained model
    final_dict = map_keys_with_calculations(converted_values)

    return final_dict


def map_keys_with_calculations(output_dict):
    """
    Map keys in the output dictionary to desired labels and calculate additional variables.

    Args:
    - output_dict: Dictionary containing variable names as keys and their corresponding values

    Returns:
    - A dictionary containing mapped keys, additional variables, and their corresponding values
    """
    mapping = {
        'list-price': 'List Price',
        'bed-room': 'Bed Room',
        'extra-space': 'Extra Space',
        'wash-room': 'Wash Room',
        'kitchen': 'Kitchen',
        'Family_Room_N': 'Family_Room_N',
        'Family_Room_Y': 'Family_Room_Y',
        'community': 'Community Encoded',
        'garage-type': 'Garage_Type_Frequency_Encoded',
        'style': 'Style_Frequency_Encoded'
    }
    
    mapped_dict = {}
    for key, value in mapping.items():
        mapped_dict[value] = output_dict.get(key, None)
    
    # Calculate additional variables
    bed_room = output_dict.get('bed-room', 0)
    wash_room = output_dict.get('wash-room', 0)
    extra_space = output_dict.get('extra-space', 0)
    kitchen = output_dict.get('kitchen', 0)
    
    mapped_dict['Bedrooms_to_Washrooms_Ratio'] = bed_room / wash_room if wash_room != 0 else 0
    mapped_dict['Total_Spaces'] = bed_room + extra_space + kitchen + wash_room
    
    return mapped_dict

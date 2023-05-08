import pickle
import streamlit as st
import numpy as np
import tensorflow
import pandas as pd
from keras.models import load_model
from PIL import Image
from streamlit_option_menu import option_menu
import matplotlib.pyplot as plt
from streamlit import session_state as ss

# load trained model
loaded_model = pickle.load(open("C:/Users/Aishwarya Kanish/PycharmProjects/pythonProject2/trained_model.pkl",'rb'))
# Load the encoder model
loaded_encoder = pickle.load(open("C:/Users/Aishwarya Kanish/PycharmProjects/pythonProject2/encoder_model.pkl",'rb'))

#creating a function for prediction
def breakfast_prakriti_prediction(new_data):

    new_df = pd.DataFrame([new_data])
    # Use OneHotEncoder to convert the new data to numerical data
    new_encoded = loaded_encoder.transform(new_df)
    # Predict the class of the new data
    y_pred_new = loaded_model.predict(new_encoded)
    print("Predicted class for new data: {}".format(y_pred_new[0]))


    # Define diet recommendations based on the predicted body state
    if y_pred_new[0] == "Vata":
        st.markdown(f'<p style="text-align:center;"><img src="https://draxe.com/wp-content/uploads/2019/03/Vata_800x365_Header.jpg" alt="vata image" width="800"></p>',unsafe_allow_html=True)
        diet_recommendations = "Your constitution is mostly comprised of Vata, and it is recommended that you reduce the qualities of cold, dryness and lightness. Here are some diet recommendations based on the season:\n\nDuring Spring/Summer:\n- Waking (½ an hour before meal): Warm tea with adaptogen herbs and culinary spices such as fennel, clove, etc.\n- Breakfast: Sweet fruit (not too cooling) or sprouted grains.\n- Snack: Sweet treats such as fruits with warming spices and herbs.\n\nDuring Fall/Winter:\n- Waking (½ an hour before meal): Soaked almonds blended with warm milk, including saffron, turmeric, honey, and coconut sugar.\n- Breakfast: Sweet fruit salad (not too cooling), soaked grain dish like oatmeal, porridge, nut or seed milks (almond, hemp), adding cinnamon is good, eggs on Ezekiel bread, olive oil bruschetta, or 'kitchari'.\n- Snack: Tahini or almond butter, in-season fresh peaches or apricots, instant organic miso soup, beetroot dip, or sunset pate."
        return (diet_recommendations)
    elif y_pred_new[0] == "Pitta":
        st.markdown(f'<p style="text-align:center;"><img src="https://draxe.com/wp-content/uploads/2019/03/Pitta_800x365_Header.jpg" alt="pitta image" width="800"></p>',unsafe_allow_html=True)
        diet_recommendations = "Your constitution is mostly comprised of Pitta, and it is recommended that you reduce the qualities of hot, dryness and lightness. Here are some diet recommendations based on the season:\n\nDuring Spring/Summer:\n- Waking (½ an hour before meal): Warm tea (herb tea such as turmeric, fennel, coriander).\n- Breakfast: Soaked almonds blended with warm milk, including saffron, turmeric, honey, coconut sugar.\n- Snack: Sweet or bitter fruit in season such as pears with blueberries, hummus with flax, edamame dip.\n\nDuring Fall/Winter:\n- Waking (½ an hour before meal): Soaked almonds blended with warm milk, including saffron, turmeric, honey, coconut sugar.\n- Breakfast: Soaked grain dish with coriander or fennel, okra, koki (Sindhi style flat-breads).\n- Snack: Apple or pear (as the cooking nature, cools the mind and emotions)."
        return (diet_recommendations)

    elif y_pred_new[0] == "Kapha":
        st.markdown(f'<p style="text-align:center;"><img src="https://draxe.com/wp-content/uploads/2019/03/Kapha_800x365_Header.jpg" alt="kapha image" width="800"></p>',unsafe_allow_html=True)
        diet_recommendations = "Your constitution is mostly comprised of Kapha, it is recommended that you reduce the qualities of cold, wetness and heaviness. Here are some diet recommendations based on the season:\n\nDuring Spring/Summer:\n- Breakfast: Ginger and licorice root tea. *Note that Kapha types may find it beneficial to skip breakfast.\n- Snack: Sour treat such as a bowl of cranberries, with warming herbs and spices.\n\nDuring Fall/Winter:\n- Breakfast: Grain dish with a cup of ginger tea. A honey, ginger and lemon concoction could also be beneficial.\n- Snack: Fresh peaches or apricots in season, with a warming spicy sauce."
        return (diet_recommendations)

#creating a function for prediction
def lunch_prakriti_prediction(new_data):

    new_df = pd.DataFrame([new_data])
    # Use OneHotEncoder to convert the new data to numerical data
    new_encoded = loaded_encoder.transform(new_df)
    # Predict the class of the new data
    y_pred_new = loaded_model.predict(new_encoded)
    print("Predicted class for new data: {}".format(y_pred_new[0]))

    # Define diet recommendations based on the predicted body state
    if y_pred_new[0] == "Vata":
        st.markdown(f'<p style="text-align:center;"><img src="https://draxe.com/wp-content/uploads/2019/03/Vata_800x365_Header.jpg" alt="vata image" width="800"></p>',unsafe_allow_html=True)
        diet_recommendations = "Your constitution is mostly comprised of Vata, it is recommended that you reduce the qualities of cold, dryness and lightness. Here are some lunch recommendations based on the season:\n\nDuring Spring/Summer:\n- Lunch: Sprouted wild rice or soaked buckwheat groats with yellowishorgans sweet root veggies. (sweet potato, yam, squash, pumpkin)\n- Snack: Sesame seed and fennel treat, raw chocolate bars, aduki hummus, edamame hummus, spiced greek yoghurt dip.\n\nDuring Fall/Winter:\n- Lunch: Fresh kale or collard salad, spinach salad (with olive oil and lemon dressing), hemp seed oil, tamarin and warming spices, flax crackers, ‘kitchari’ stew, warmed salmon, paneer masala, okra masala, thai\n- Snack: Apple sauce with cinnamon, nutmeg and sweetened with honey, spicy herbal tea, miso soup, goji berry mix."
        return (diet_recommendations)
    elif y_pred_new[0] == "Pitta":
        #st.image("pitta.jpg", use_column_width=True)
        st.markdown(f'<p style="text-align:center;"><img src="https://draxe.com/wp-content/uploads/2019/03/Pitta_800x365_Header.jpg" alt="pitta image" width="800"></p>',unsafe_allow_html=True)
        diet_recommendations = "Your constitution is mostly comprised of Pitta, it is recommended that you reduce the qualities of hot, dryness and lightness. Here are some lunch and snack recommendations based on the season:\n\nDuring Spring/Summer:\n- Lunch: Sprouted barley or kamut grans with cabbage or broccoli, bitter green salad with lemon olive oil dressing, salad with sprouts, broccoli and chickpea stir fry.\n- Snack: Sunflower seeds, fennel and lemon grass tea, tamari brown rice crackers.\n\nDuring Fall/Winter:\n- Lunch: Fresh kale or collard salad with lemon or lime dressing & sunflower oil, steamed greens and tofu with tamarin and cooling herbs, herbed flax seed crackers with Indian style dhal, ‘kitchari’ stew, warmed sole, okra masala, paneer masala, thai green curry with cruciferous vegetables.\n- Snack: Apple sauce with cinnamon, nutmeg and sweetened with stevia, miso soup with pumpkin, mint tea."
        return ("Diet recommendations based on predicted body state: ", diet_recommendations)
    elif y_pred_new[0] == "Kapha":
        #st.image("kapha.jpeg", use_column_width=True)
        st.markdown(f'<p style="text-align:center;"><img src="https://draxe.com/wp-content/uploads/2019/03/Kapha_800x365_Header.jpg" alt="kapha image" width="800"></p>',unsafe_allow_html=True)
        diet_recommendations = "Your constitution is mostly comprised of Kapha, it is recommended that you reduce the qualities of cold, wetness and heaviness. Here are some diet recommendations based on the season:\n\nDuring Spring/Summer:\n- Lunch: Sprouted barley with sauce, blackeye pea succotash, cauliflower rice in Thai ginger sauce, fresh celery soup, fresh green salad with pomegranates.\n- Snack: Raspberries, lemongrass tea.\n\nDuring Fall/Winter:\n- Lunch: Fresh kale or collard salad with lemon or lime dressing & sunflower oil, soaked buckwheat and fresh Brussels sprouts salad marinated with sesame oil and mustard seeds oil, Sprouted grain and flax seeds crackers with aduki bean and black pepper hummus, Thai style cauliflower rice with ginger sauce.\n- Snack: Pumpkin seeds, cup of saffron almond milk or herbal tea."
        return ("Diet recommendations based on predicted body state: ", diet_recommendations)

#creating a function for prediction
def dinner_prakriti_prediction(new_data):

    new_df = pd.DataFrame([new_data])
    # Use OneHotEncoder to convert the new data to numerical data
    new_encoded = loaded_encoder.transform(new_df)
    # Predict the class of the new data
    y_pred_new = loaded_model.predict(new_encoded)
    print("Predicted class for new data: {}".format(y_pred_new[0]))

    # Define diet recommendations based on the predicted body state
    if y_pred_new[0] == "Vata":
        st.markdown(f'<p style="text-align:center;"><img src="https://draxe.com/wp-content/uploads/2019/03/Vata_800x365_Header.jpg" alt="vata image" width="800"></p>',unsafe_allow_html=True)
        diet_recommendations = "Your constitution is mostly comprised of Vata, it is recommended that you reduce the qualities of cold, dryness and lightness. Here are some diet recommendations based on the season:\n\nDuring Spring/Summer:\n- Dinner: Spaghetti squash with fresh tomato sauce, zucchini pasta, Thai fried brown rice, tom yum vegetarian soup, Thai green curry with veggies, Baked Eggplant with avocado sauce.\n- Snack: Carob brownie, dark chocolate raw treat.\n- Bedtime: Warm nervine tea with ginger and honey.\n\nDuring Fall/Winter:\n- Dinner: Stir fry root vegetables with ginger dipping sauce, warm mushroom broth with wontons and buckwheat noodles, rice noodles pad thai style, vegetarian sate with peanut dipping sauce.\n- Snack: Pumpkin pudding, culinary seed tea.\n- Bedtime: Warm spicy toddy with vanilla and carob meal, warm homemade almond milk with honey and saffron."
        return (diet_recommendations)
    elif y_pred_new[0] == "Pitta":
        #st.image("pitta.jpg", use_column_width=True)
        st.markdown(f'<p style="text-align:center;"><img src="https://draxe.com/wp-content/uploads/2019/03/Pitta_800x365_Header.jpg" alt="pitta image" width="800"></p>',unsafe_allow_html=True)
        diet_recommendations = "Your constitution is mostly comprised of Pitta, it is recommended that you reduce the qualities of hot, dryness and lightness. Here are some diet recommendations based on the season:\n\nDuring Spring/Summer:\n- Dinner: Cauliflower and Jerusalem artichoke dish with a spicy cilantro sauce, zucchini pasta with a fresh tomato sauce, cauliflower fried rice, mung lentils and ata chapatis.\n- Snack: Coconut macaroons with red clover tea, coconut beetroot pudding.\n\nDuring Fall/Winter:\n- Dinner: Stir fry root vegetables with coriander dipping sauce, cooling kombu mushroom broth with wontons and buckwheat noodles, chickpea curry with sesame seeds and sunflower seed butters, flax crackers with caraway seeds and beetroot dip.\n- Snack: Pumpkin pudding, catnip tea."
        return (diet_recommendations)
    elif y_pred_new[0] == "Kapha":
        #st.image("kapha.jpeg", use_column_width=True)
        st.markdown(f'<p style="text-align:center;"><img src="https://draxe.com/wp-content/uploads/2019/03/Kapha_800x365_Header.jpg" alt="kapha image" width="800"></p>',unsafe_allow_html=True)
        diet_recommendations = "Your constitution is mostly comprised of Kapha, it is recommended that you reduce the qualities of cold, wetness and heaviness. Here are some diet recommendations based on the season:\n\nDuring Spring/Summer:\n- Dinner: Cauliflower and Jerusalem artichoke dish with a spicy cilantro sauce, zucchini pasta with a fresh tomato sauce, cauliflower fried rice, mung lentils and ata chapatis, root vegetable and burdock stir fry with curry and cumin sauce, dark green salad.\n- Snack: Cranberry dessert.\n\nDuring Fall/Winter:\n- Dinner: Stir fry root vegetables with coriander dipping sauce, heating kombu mushroom broth with millet, quinoa patties with spicy relish, Mexican Sprouted Ezekiel wraps with aduki beans.\n- Snack: Sour apple and chamomile tea."
        return (diet_recommendations)

st.set_page_config(page_title="AyurFoodie Recommender System", page_icon=":apple:", layout="wide")
# Define the introduction text
home_text = f"""
    ## Welcome to AyurFoodie Recommender System!

    This is a diet recommender system based on Ayurvedic principles. Ayurveda is a traditional system of medicine that originated in India and has been practiced for thousands of years. It emphasizes the importance of balancing the three doshas: Vata, Pitta, and Kapha.

    AyurFoodie Recommender System is designed to help you choose the right foods for your dosha type. To get started, select a meal from the menu on the left and we'll recommend some delicious, Ayurvedic recipes for you to try.
"""
    # Display the home page
st.write(home_text)
ss.page_index = 0

with st.sidebar:

    selected = option_menu("AyurFoodie's Diet Recommender",
                           ['Breakfast',
                            'Lunch',
                            'Dinner'],
                           icons =['cloud','cloud-sun','cloud-moon'],
                           default_index=0)

#Ayurvedic Diet Recommendation Page
if (selected == 'Breakfast'):
    #page title
    #st.title('Personalized Ayurvedic Breakfast Diet')

    #st.markdown("<div align='center'><div style='background-color:#F5DEB3; padding:10px'><h2 style='font-family:Arial, sans-serif; color:#008080;'>Personalized Ayurvedic Breakfast Diet</h2></div>",unsafe_allow_html=True)
    st.markdown("<div align='center'><div style='background-color:#FFE4B5; padding:10px'><h2 style='font-family:Arial, sans-serif; color:#000080;'>Get Your Personalized Breakfast Diet </h2></div></div>",unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 1, 1])
    # Define the flex layout for the columns
    st.markdown(
        f"""
        <style>
        .stHorizontal > div:not(:last-child) {{
            margin-right: 50px;
        }}
        .stHorizontal > div {{
            width: calc((100% - 100px) / 3);
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

    with col1:
        st.write("")  # placeholder to align the column
        st.write("")
        body_frame = st.selectbox("**Body Frame**", ('Thin and Lean', 'Medium', 'Well Built'),key='body_frame')
        weight = st.selectbox("**Weight**", ('Low, Difficult to Put on Weight', 'Medium, Can Easily Lose or Gain Weight','Overweight, Difficult to Lose Weight'))
        skin_color = st.selectbox("**Skin Color and Complexion**", ('Dark, Blackish', 'Pink to Red', 'Glowing, White'))
        skin_charac = st.selectbox("**Skin Characteristics**", ('Dry, Rough', 'Delicate, irritable skin prone to rashes and pimples', 'Slightly oily, Smooth, thick skin'))
        sweat = st.selectbox("**Sweat**",('scanty even in heat', 'sweat even in cold weather', 'sweat is moderate and consistent'))
        head_hair = st.selectbox("**Head Hair**", ('Dry, Very Curly and with Splits End', 'Thin, Quite Straight and early baldness','Greasy, slightly wavy and thick'))
        nails = st.selectbox("**Nails**", ('hard, brittle nails that are rough and may differ in size.', 'soft, strong, somewhat rubbery and well formed','strong, large and symmetrical'))
        eyeball = st.selectbox("**Eyeball**", ('Unsteady, Fast Moving', 'Moving Slowly', 'Calm and Steady'))
        teeth_size = st.selectbox("**Size and Teeth Color**", ('Crooked or Uneven teeth, grayish in color', 'Even teeth of medium size, Yellow, Orange or Red','Large, even, gleaming teeth, Shinning White'))
        eating_habit = st.selectbox("**Eating Habit**", ('Eats Quickly Without Chewing Properly', 'Eats at a Moderate Speed', 'Chews Food Properly'))
    with col2:
        st.write("")  # placeholder to align the column
        st.write("")
        hunger = st.selectbox("**Hunger**",('Irregular, Any Time', 'Sudden Hunger Pangs, Sharp Hunger', 'Can Skip any Meal Easily'))
        bowel_move = st.selectbox("**Bowel Movements**", ('Dry, Hard, Blackish,Scanty Stools', 'Soft, Yellowish, Loose Stools', 'Heavy, Thick, Stick Stools'))
        intolerance = st.selectbox("**Intolerance to Weather Conditions**",('Aversion to Cold', 'Aversion to Heat', 'Aversion to Moist, Rainy and Cool Weather'))
        mood = st.selectbox("**Mood**", ('Changes quickly have frequent mood swings', 'Changes Slowly', 'Stable Constant'))
        body_energy = st.selectbox("**Body Energy**", ('Becomes Low in Evening, Fatigues After Less Work', 'Moderate, Gets Tired After Medium Work','Excellent Energy Throughout day not easily Fatigued'))
        pulse = st.selectbox("**Pulse**", ('Thin, Shallow and Fast with a Broken or Variable rhythm','Full, Regular, and Strong, with medium speed and rhythm','Strong, Full, Slow and rhythm'))
        sleep = st.selectbox("**Sleep**", ('Interrupted, Less', 'Moderate', 'Sleep heavily, Lazy'))
        dreams = st.selectbox("**Dreams**", ('Dream a lot, often violent and forget their dreams easily','Dreams are passionate and remember what they dream','Dreams are cool, peaceful and do not bother to remember such dreams'))
        communication = st.selectbox("**Communication Skills**", ('Speak quickly, often with rising pitch at the end of a phase', 'Concise and one-pointed in what they say','Speak slowly and cautiously, without volunteering much.'))
        voice_quality = st.selectbox("**Quality of Voice**", ('Rough with broken words', 'Commanding', 'Soft and Deep'))
    with col3:
        st.write("")  # placeholder to align the column
        st.write("")
        social_relations = st.selectbox("**Social Relations**", ('Make Less Friends, Prefers Solitude', 'Good No. of Friends','Love to Socialize, Relationships are Longer Lasting'))
        mental_activity = st.selectbox("**Mental Activity**",('Quick, Restless', 'Smart Intellect, Aggressive', 'Calm, Stable'))
        memory = st.selectbox("**Memory**", ('Short Term, Bad', 'Good Memory', 'Long Term, Best'))
        grasping_power = st.selectbox("**Grasping Power**", ('Grasps quickly but not completely and forgets quickly', 'Grasps quickly but completely and have good memory','Grasps late and retains for longer time'))
        joints = st.selectbox("**Joints**",('Weak, Noise on Movements', 'Healthy with Optimal Strength', 'Heavy Weight Bearing'))
        walking_pace = st.selectbox("**Walking Pace**",('Quick, Fast with Long Steps', 'Average Steady', 'Slow with Short steps'))
        nature = st.selectbox("**Nature**", ('Timid, Jealous', 'Egoistic, Fearless', 'Forgiving, Greatful, Not Greedy'))
        wealth = st.selectbox("**Wealth**", ('Spends without thinking much', 'Saves but spends on valuable things', 'Prefers more savings'))
        work_performance = st.selectbox("**Pace of Performing Work**",('Fast, Always in Hurry', 'Medium, Energetic', 'Slow, Steady'))
        body_temp = st.selectbox("**Body Temperature**", ('Less than Normal, Hand and Feets are cold', 'More than Normal, Face and Forehead Hot','Normal, Hands and Feets Slightly Cold'))


    # Code for Prediction
    Prediction = ' '



    # creating a button to predict the output
    if st.button('Prediction Result 👀'):  # if st.markdown("""<div style='text-align: center;'><button>Prediction Result 👀</button></div>""",unsafe_allow_html=True):
        new_data = {
            'Body Frame': body_frame,
            'Weight': weight,
            'Skin Color and Complexion': skin_color,
            'Skin Characteristics': skin_charac,
            'Sweat': sweat,
            'Head Hair': head_hair,
            'Nails': nails,
            'Eyeball': eyeball,
            'Size and Teeth Color': teeth_size,
            'Eating Habit': eating_habit,
            'Hunger': hunger,
            'Bowel Movements': bowel_move,
            'Intolerance to Weather Conditions': intolerance,
            'Mood': mood,
            'Body Energy': body_energy,
            'Pulse': pulse,
            'Sleep': sleep,
            'Dreams': dreams,
            'Communication Skills': communication,
            'Quality of Voice': voice_quality,
            'Social Relations': social_relations,
            'Mental Activity': mental_activity,
            'Memory': memory,
            'Grasping Power': grasping_power,
            'Joints': joints,
            'Walking Pace': walking_pace,
            'Nature': nature,
            'Wealth': wealth,
            'Pace of Performing Work': work_performance,
            'Body Temperature': body_temp}

        Prediction = breakfast_prakriti_prediction(new_data)

    st.success(Prediction)

    # Center the button using CSS
    st.markdown("""
        <style>
            div.stButton > button:first-child {
                margin-left: auto;
                margin-right: auto;
                display: block;
            }
        </style>
    """, unsafe_allow_html=True)

#-------------------------------------------------------------------------------------------------------------------------

if (selected == 'Lunch'):
    # page title
    #st.title('Personalized Ayurvedic Lunch Diet')
    st.markdown(
        "<div align='center'><div style='background-color:#FFE4B5; padding:10px'><h2 style='font-family:Arial, sans-serif; color:#000080;'>Get Your Personalized Lunch Diet </h2></div></div>",
        unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 1, 1])
    # Define the flex layout for the columns
    st.markdown(
        f"""
            <style>
            .stHorizontal > div:not(:last-child) {{
                margin-right: 50px;
            }}
            .stHorizontal > div {{
                width: calc((100% - 100px) / 3);
            }}
            </style>
            """,
        unsafe_allow_html=True
    )

    with col1:
        st.write("")  # placeholder to align the column
        st.write("")
        body_frame = st.selectbox("**Body Frame**", ('Thin and Lean', 'Medium', 'Well Built'))
        weight = st.selectbox("**Weight**", ('Low, Difficult to Put on Weight', 'Medium, Can Easily Lose or Gain Weight','Overweight, Difficult to Lose Weight'))
        skin_color = st.selectbox("**Skin Color and Complexion**", ('Dark, Blackish', 'Pink to Red', 'Glowing, White'))
        skin_charac = st.selectbox("**Skin Characteristics**", ('Dry, Rough', 'Delicate, irritable skin prone to rashes and pimples', 'Slightly oily, Smooth, thick skin'))
        sweat = st.selectbox("**Sweat**",('scanty even in heat', 'sweat even in cold weather', 'sweat is moderate and consistent'))
        head_hair = st.selectbox("**Head Hair**", ('Dry, Very Curly and with Splits End', 'Thin, Quite Straight and early baldness','Greasy, slightly wavy and thick'))
        nails = st.selectbox("**Nails**", ('hard, brittle nails that are rough and may differ in size.', 'soft, strong, somewhat rubbery and well formed','strong, large and symmetrical'))
        eyeball = st.selectbox("**Eyeball**", ('Unsteady, Fast Moving', 'Moving Slowly', 'Calm and Steady'))
        teeth_size = st.selectbox("**Size and Teeth Color**", ('Crooked or Uneven teeth, grayish in color', 'Even teeth of medium size, Yellow, Orange or Red','Large, even, gleaming teeth, Shinning White'))
        eating_habit = st.selectbox("**Eating Habit**", ('Eats Quickly Without Chewing Properly', 'Eats at a Moderate Speed', 'Chews Food Properly'))
    with col2:
        st.write("")  # placeholder to align the column
        st.write("")
        hunger = st.selectbox("**Hunger**",('Irregular, Any Time', 'Sudden Hunger Pangs, Sharp Hunger', 'Can Skip any Meal Easily'))
        bowel_move = st.selectbox("**Bowel Movements**", ('Dry, Hard, Blackish,Scanty Stools', 'Soft, Yellowish, Loose Stools', 'Heavy, Thick, Stick Stools'))
        intolerance = st.selectbox("**Intolerance to Weather Conditions**", ('Aversion to Cold', 'Aversion to Heat', 'Aversion to Moist, Rainy and Cool Weather'))
        mood = st.selectbox("**Mood**",('Changes quickly have frequent mood swings', 'Changes Slowly', 'Stable Constant'))
        body_energy = st.selectbox("**Body Energy**", ('Becomes Low in Evening, Fatigues After Less Work', 'Moderate, Gets Tired After Medium Work','Excellent Energy Throughout day not easily Fatigued'))
        pulse = st.selectbox("**Pulse**", ('Thin, Shallow and Fast with a Broken or Variable rhythm','Full, Regular, and Strong, with medium speed and rhythm','Strong, Full, Slow and rhythm'))
        sleep = st.selectbox("**Sleep**", ('Interrupted, Less', 'Moderate', 'Sleep heavily, Lazy'))
        dreams = st.selectbox("**Dreams**", ('Dream a lot, often violent and forget their dreams easily','Dreams are passionate and remember what they dream','Dreams are cool, peaceful and do not bother to remember such dreams'))
        communication = st.selectbox("**Communication Skills**", ('Speak quickly, often with rising pitch at the end of a phase', 'Concise and one-pointed in what they say','Speak slowly and cautiously, without volunteering much.'))
        voice_quality = st.selectbox("**Quality of Voice**", ('Rough with broken words', 'Commanding', 'Soft and Deep'))
    with col3:
        st.write("")  # placeholder to align the column
        st.write("")
        social_relations = st.selectbox("**Social Relations**", ('Make Less Friends, Prefers Solitude', 'Good No. of Friends','Love to Socialize, Relationships are Longer Lasting'))
        mental_activity = st.selectbox("**Mental Activity**",('Quick, Restless', 'Smart Intellect, Aggressive', 'Calm, Stable'))
        memory = st.selectbox("**Memory**", ('Short Term, Bad', 'Good Memory', 'Long Term, Best'))
        grasping_power = st.selectbox("**Grasping Power**", ('Grasps quickly but not completely and forgets quickly', 'Grasps quickly but completely and have good memory','Grasps late and retains for longer time'))
        joints = st.selectbox("**Joints**", ('Weak, Noise on Movements', 'Healthy with Optimal Strength', 'Heavy Weight Bearing'))
        walking_pace = st.selectbox("**Walking Pace**",('Quick, Fast with Long Steps', 'Average Steady', 'Slow with Short steps'))
        nature = st.selectbox("**Nature**", ('Timid, Jealous', 'Egoistic, Fearless', 'Forgiving, Greatful, Not Greedy'))
        wealth = st.selectbox("**Wealth**",('Spends without thinking much', 'Saves but spends on valuable things', 'Prefers more savings'))
        work_performance = st.selectbox("**Pace of Performing Work**",('Fast, Always in Hurry', 'Medium, Energetic', 'Slow, Steady'))
        body_temp = st.selectbox("**Body Temperature**", ('Less than Normal, Hand and Feets are cold', 'More than Normal, Face and Forehead Hot','Normal, Hands and Feets Slightly Cold'))

    # Code for Prediction
    Prediction = ' '
    # creating a button to predict the output
    if st.button(
            'Prediction Result 👀'):  # if st.markdown("""<div style='text-align: center;'><button>Prediction Result 👀</button></div>""",unsafe_allow_html=True):
        new_data = {
            'Body Frame': body_frame,
            'Weight': weight,
            'Skin Color and Complexion': skin_color,
            'Skin Characteristics': skin_charac,
            'Sweat': sweat,
            'Head Hair': head_hair,
            'Nails': nails,
            'Eyeball': eyeball,
            'Size and Teeth Color': teeth_size,
            'Eating Habit': eating_habit,
            'Hunger': hunger,
            'Bowel Movements': bowel_move,
            'Intolerance to Weather Conditions': intolerance,
            'Mood': mood,
            'Body Energy': body_energy,
            'Pulse': pulse,
            'Sleep': sleep,
            'Dreams': dreams,
            'Communication Skills': communication,
            'Quality of Voice': voice_quality,
            'Social Relations': social_relations,
            'Mental Activity': mental_activity,
            'Memory': memory,
            'Grasping Power': grasping_power,
            'Joints': joints,
            'Walking Pace': walking_pace,
            'Nature': nature,
            'Wealth': wealth,
            'Pace of Performing Work': work_performance,
            'Body Temperature': body_temp}

        Prediction = lunch_prakriti_prediction(new_data)

    st.success(Prediction)
    # Center the button using CSS
    st.markdown("""
            <style>
                div.stButton > button:first-child {
                    margin-left: auto;
                    margin-right: auto;
                    display: block;
                }
            </style>
        """, unsafe_allow_html=True)
#------------------------------------------------------------------------------------------------------------------------------

if (selected == 'Dinner'):
    # page title
    #st.title('Personalized Ayurvedic Dinner Diet')
    st.markdown(
        "<div align='center'><div style='background-color:#FFE4B5; padding:10px'><h2 style='font-family:Arial, sans-serif; color:#000080;'>Get Your Personalized Dinner Diet</h2></div></div>",
        unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 1, 1])
    # Define the flex layout for the columns
    st.markdown(
        f"""
            <style>
            .stHorizontal > div:not(:last-child) {{
                margin-right: 50px;
            }}
            .stHorizontal > div {{
                width: calc((100% - 100px) / 3);
            }}
            </style>
            """,
        unsafe_allow_html=True
    )

    with col1:
        st.write("")  # placeholder to align the column
        st.write("")
        body_frame = st.selectbox("**Body Frame**", ('Thin and Lean', 'Medium', 'Well Built'), key='body_frame')
        weight = st.selectbox("**Weight**", ('Low, Difficult to Put on Weight', 'Medium, Can Easily Lose or Gain Weight','Overweight, Difficult to Lose Weight'))
        skin_color = st.selectbox("**Skin Color and Complexion**", ('Dark, Blackish', 'Pink to Red', 'Glowing, White'))
        skin_charac = st.selectbox("**Skin Characteristics**", ('Dry, Rough', 'Delicate, irritable skin prone to rashes and pimples', 'Slightly oily, Smooth, thick skin'))
        sweat = st.selectbox("**Sweat**",('scanty even in heat', 'sweat even in cold weather', 'sweat is moderate and consistent'))
        head_hair = st.selectbox("**Head Hair**", ('Dry, Very Curly and with Splits End', 'Thin, Quite Straight and early baldness','Greasy, slightly wavy and thick'))
        nails = st.selectbox("**Nails**", ('hard, brittle nails that are rough and may differ in size.', 'soft, strong, somewhat rubbery and well formed','strong, large and symmetrical'))
        eyeball = st.selectbox("**Eyeball**", ('Unsteady, Fast Moving', 'Moving Slowly', 'Calm and Steady'))
        teeth_size = st.selectbox("**Size and Teeth Color**", ('Crooked or Uneven teeth, grayish in color', 'Even teeth of medium size, Yellow, Orange or Red','Large, even, gleaming teeth, Shinning White'))
        eating_habit = st.selectbox("**Eating Habit**", ('Eats Quickly Without Chewing Properly', 'Eats at a Moderate Speed', 'Chews Food Properly'))
    with col2:
        st.write("")  # placeholder to align the column
        st.write("")
        hunger = st.selectbox("**Hunger**",('Irregular, Any Time', 'Sudden Hunger Pangs, Sharp Hunger', 'Can Skip any Meal Easily'))
        bowel_move = st.selectbox("**Bowel Movements**", ('Dry, Hard, Blackish,Scanty Stools', 'Soft, Yellowish, Loose Stools', 'Heavy, Thick, Stick Stools'))
        intolerance = st.selectbox("**Intolerance to Weather Conditions**", ('Aversion to Cold', 'Aversion to Heat', 'Aversion to Moist, Rainy and Cool Weather'))
        mood = st.selectbox("**Mood**",('Changes quickly have frequent mood swings', 'Changes Slowly', 'Stable Constant'))
        body_energy = st.selectbox("**Body Energy**", ('Becomes Low in Evening, Fatigues After Less Work', 'Moderate, Gets Tired After Medium Work','Excellent Energy Throughout day not easily Fatigued'))
        pulse = st.selectbox("**Pulse**", ('Thin, Shallow and Fast with a Broken or Variable rhythm','Full, Regular, and Strong, with medium speed and rhythm','Strong, Full, Slow and rhythm'))
        sleep = st.selectbox("**Sleep**", ('Interrupted, Less', 'Moderate', 'Sleep heavily, Lazy'))
        dreams = st.selectbox("**Dreams**", ('Dream a lot, often violent and forget their dreams easily','Dreams are passionate and remember what they dream','Dreams are cool, peaceful and do not bother to remember such dreams'))
        communication = st.selectbox("**Communication Skills**", ('Speak quickly, often with rising pitch at the end of a phase', 'Concise and one-pointed in what they say','Speak slowly and cautiously, without volunteering much.'))
        voice_quality = st.selectbox("**Quality of Voice**", ('Rough with broken words', 'Commanding', 'Soft and Deep'))
    with col3:
        st.write("")  # placeholder to align the column
        st.write("")
        social_relations = st.selectbox("**Social Relations**", ('Make Less Friends, Prefers Solitude', 'Good No. of Friends','Love to Socialize, Relationships are Longer Lasting'))
        mental_activity = st.selectbox("**Mental Activity**",('Quick, Restless', 'Smart Intellect, Aggressive', 'Calm, Stable'))
        memory = st.selectbox("**Memory**", ('Short Term, Bad', 'Good Memory', 'Long Term, Best'))
        grasping_power = st.selectbox("**Grasping Power**", ('Grasps quickly but not completely and forgets quickly', 'Grasps quickly but completely and have good memory','Grasps late and retains for longer time'))
        joints = st.selectbox("**Joints**",('Weak, Noise on Movements', 'Healthy with Optimal Strength', 'Heavy Weight Bearing'))
        walking_pace = st.selectbox("**Walking Pace**",('Quick, Fast with Long Steps', 'Average Steady', 'Slow with Short steps'))
        nature = st.selectbox("**Nature**", ('Timid, Jealous', 'Egoistic, Fearless', 'Forgiving, Greatful, Not Greedy'))
        wealth = st.selectbox("**Wealth**", ('Spends without thinking much', 'Saves but spends on valuable things', 'Prefers more savings'))
        work_performance = st.selectbox("**Pace of Performing Work**",('Fast, Always in Hurry', 'Medium, Energetic', 'Slow, Steady'))
        body_temp = st.selectbox("**Body Temperature**", ('Less than Normal, Hand and Feets are cold', 'More than Normal, Face and Forehead Hot','Normal, Hands and Feets Slightly Cold'))

    # Code for Prediction
    Prediction = ' '
    # creating a button to predict the output
    if st.button(
            'Prediction Result 👀'):  # if st.markdown("""<div style='text-align: center;'><button>Prediction Result 👀</button></div>""",unsafe_allow_html=True):
        new_data = {
            'Body Frame': body_frame,
            'Weight': weight,
            'Skin Color and Complexion': skin_color,
            'Skin Characteristics': skin_charac,
            'Sweat': sweat,
            'Head Hair': head_hair,
            'Nails': nails,
            'Eyeball': eyeball,
            'Size and Teeth Color': teeth_size,
            'Eating Habit': eating_habit,
            'Hunger': hunger,
            'Bowel Movements': bowel_move,
            'Intolerance to Weather Conditions': intolerance,
            'Mood': mood,
            'Body Energy': body_energy,
            'Pulse': pulse,
            'Sleep': sleep,
            'Dreams': dreams,
            'Communication Skills': communication,
            'Quality of Voice': voice_quality,
            'Social Relations': social_relations,
            'Mental Activity': mental_activity,
            'Memory': memory,
            'Grasping Power': grasping_power,
            'Joints': joints,
            'Walking Pace': walking_pace,
            'Nature': nature,
            'Wealth': wealth,
            'Pace of Performing Work': work_performance,
            'Body Temperature': body_temp}

        Prediction = dinner_prakriti_prediction(new_data)

    st.success(Prediction)
    # Center the button using CSS
    st.markdown("""
            <style>
                div.stButton > button:first-child {
                    margin-left: auto;
                    margin-right: auto;
                    display: block;
                }
            </style>
        """, unsafe_allow_html=True)










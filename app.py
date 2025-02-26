#streamlit
import streamlit as st

st.set_page_config(page_title="Growth Mindset Simulation")
st.title(" 🌃 Growth Mindest Simulation")

st.header("Growth is not the destination but an endless journey! 😉")
st.write("Learning is a never ending process. This AI powered app helps you discover your growth potential")

# Why Adopt a Growth Mindset?
st.header("Why Adopt a Growth Mindset?")
benefits = [
    "💪 **Embrace Challenges** - View obstacles as learning opportunities.",
    "🛠 **Learn from Mistakes** - Understand that mistakes are a part of growth.",
    "🚀 **Persist Through Difficulties** - Stay determined even when things get tough.",
    "🎉 **Celebrate Effort** - Value the process of learning, not just the result.",
    "🔎 **Keep an Open Mind** - Stay curious and adaptable."
]
st.write("\n".join(benefits))

st.header("How Can You Practice a Growth Mindset?")
steps = [
    "1️⃣ **Set Learning Goals** - Focus on skills instead of just grades.",
    "2️⃣ **Reflect on Your Learning** - Think about what you've learned from successes and failures.",
    "3️⃣ **Seek Feedback** - Use criticism as a tool for improvement.",
    "4️⃣ **Stay Positive** - Believe in your ability to grow."
]
st.write("\n".join(steps))


st.header("📝 Quick Growth Mindset Quiz")
questions = [
    ("Do you believe intelligence is fixed? (Yes/No)", "No"),
    ("How do you handle failure? (Give up / Learn from it)", "Learn from it"),
    ("What matters more: Effort or Talent?", "Effort")]

score = 0
for q, correct_answer in questions:
    user_answer = st.radio(q, options=["Yes", "No"] if "Yes" in q else ["Give up", "Learn from it"] if "failure" in q else ["Effort", "Talent"])
    if user_answer == correct_answer:
        score += 1

st.write(f"🎯 Your Growth Mindset Score: **{score}/{len(questions)}**")


#Quote
st.header(" 💡 Quote of the day!")
st.write("Whatever makes you uncomfortable is your biggest opportunity for growth. 🔐 -Bryant-H-Mcgill")

st.header("What problem are you facing! Let me help you.")
user_input =st.text_input ("Identify your problem")

#Condition

if user_input:
    st.success(f"You are facing : {user_input}.Continue grinding yourself, you are near!")
else:
    st.warning("Tell me the challenge I should work on!")


#Reflexing
st.header("What were your observations")
observation=st.text_area("Write your observations here:")

if observation:
    st.success(f"Well observed! Your observation:{observation}")
else:
    st.info("A clear sight on your past experiences would help you navigate through the upcoming challenges!Share your abiguities")

#Achievement
st.header("Celebrate your achievements even if they are small")
achievement=st.text_input("Your recent accompishements!")

if achievement:
    st.success(f"Incredible! You accompished:{achievement}")
else:
    st.info("Either big or small, every accomplishement is a sign of growth!")


#footer
st.write("-   -   -")
st.write("Don't fear failiure! As long as you are working hard you are answerable to no one.")
st.write("** Ⓒ Created by Shahzaib Aslam**")



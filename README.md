# INAE_Hackathon
Hackathon - Making an Alexa like device which can tell stories for a given collection of Indian toys.

Pre-requisites: 

  1. A light-weight database (we have used MySQL), 

  2. A set of pre-installed python modules with a stable internet connection to establish a successful API call request/response to Wikipedia in order to get the              information/story of the given Indian toy as per the command given by the end user.


#################### Set Up ###########################

The code is give module-wise, you need to follow the below steps to set up the environment in your machine:

1. Install the required packages
2. Import the packages
3. Execute the invokeDevice function (from "invokeDevice.py" file)
4. Execute alexaSpeak function (from "alexaSpeak.py" file)
5. Execute the implementation function ("from implementation.py" file)
6. Execute the main function (from "main.py" file)

********************** NOTE ******************************

We are open to suggestions and improvements in our code

Thanks!




Below are the packages that need to be pre-installed as mentioned in the repoort

#installing the required packages for speech input and conversion of speech into meaningful text

pip install speechrecognition
pip install pyaudio
pip install pyttsx3

#installed wikipedia for the internal API call to wiki source
pip install wikipedia

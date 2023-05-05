# Tori-captcha (a captcha system)
A captcha system that people can register in and use to create captchas on their own websites. Also, people can check the captcha answer through APIs.
# Technologies used
![image](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![image](https://img.shields.io/badge/fastapi-109989?style=for-the-badge&logo=FASTAPI&logoColor=white)
![image](https://img.shields.io/badge/redis-CC0000.svg?&style=for-the-badge&logo=redis&logoColor=white)
![image](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)
![image](https://img.shields.io/badge/MySQL-005C84?style=for-the-badge&logo=mysql&logoColor=white)

# how does it work?
In this system, first people who need captcha register on the website and receive a token, then, using it, they call an api that creates a captcha randomly and sends the ID of that captcha as an output.
By using the ID that they received in the captcha creation stage, they can receive the captcha image and then send the user answer to another api, and if the answer is correct, they will get the correct answer.

![Diagram](./readme_files/diagram.png)

# Document
**To view the document, go to the `/docs` or `/redoc` path after running the project**

#

# How to run the project?
## Manualy
> This method is not suitable for production (Because of the last step)
```bash
# clone the project
git clone https://github.com/TorhamDev/Tori-captcha.git

cd Tori-captcha

# Install dependencies 
pip install -r requirements.txt

# run project
uvicorn main:app --reload
```

# License
[![Licence](https://img.shields.io/github/license/Ileriayo/markdown-badges?style=for-the-badge)](./LICENSE)
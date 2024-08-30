# ------------------------------- Navegação -------------------------------
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

# ------------------------------- Bibliotecas -------------------------------
from os import path, listdir, remove, mkdir
import re
from urllib import request
from time import sleep
import logging
from datetime import datetime
# ------------------------------- Funções -------------------------------


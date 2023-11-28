import os

from cs50 import SQL 
from datetime import datetime
from flask import Flask, render_template
from flask_session import Session

app = Flask(__name__)


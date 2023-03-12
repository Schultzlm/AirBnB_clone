#!/usr/bin/python3""" holds class User"""
import modelsfrom models.base_model import BaseModel, Basefrom os import getenvimport sqlalchemyfrom sqlalchemy import Column, Stringfrom sqlalchemy.orm import relationshipfrom hashlib import md5

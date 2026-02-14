{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "e2c23f2c-cef2-4403-9220-618a5be65718",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting streamlit\n",
      "  Downloading streamlit-1.54.0-py3-none-any.whl.metadata (9.8 kB)\n",
      "Collecting altair!=5.4.0,!=5.4.1,<7,>=4.0 (from streamlit)\n",
      "  Downloading altair-6.0.0-py3-none-any.whl.metadata (11 kB)\n",
      "Collecting blinker<2,>=1.5.0 (from streamlit)\n",
      "  Downloading blinker-1.9.0-py3-none-any.whl.metadata (1.6 kB)\n",
      "Collecting cachetools<7,>=5.5 (from streamlit)\n",
      "  Downloading cachetools-6.2.6-py3-none-any.whl.metadata (5.6 kB)\n",
      "Requirement already satisfied: click<9,>=7.0 in /home/cloud/anaconda3/lib/python3.12/site-packages (from streamlit) (8.1.7)\n",
      "Collecting gitpython!=3.1.19,<4,>=3.0.7 (from streamlit)\n",
      "  Downloading gitpython-3.1.46-py3-none-any.whl.metadata (13 kB)\n",
      "Requirement already satisfied: numpy<3,>=1.23 in /home/cloud/anaconda3/lib/python3.12/site-packages (from streamlit) (1.26.4)\n",
      "Requirement already satisfied: packaging>=20 in /home/cloud/anaconda3/lib/python3.12/site-packages (from streamlit) (24.1)\n",
      "Requirement already satisfied: pandas<3,>=1.4.0 in /home/cloud/anaconda3/lib/python3.12/site-packages (from streamlit) (2.2.3)\n",
      "Requirement already satisfied: pillow<13,>=7.1.0 in /home/cloud/anaconda3/lib/python3.12/site-packages (from streamlit) (11.0.0)\n",
      "Collecting pydeck<1,>=0.8.0b4 (from streamlit)\n",
      "  Downloading pydeck-0.9.1-py2.py3-none-any.whl.metadata (4.1 kB)\n",
      "Requirement already satisfied: protobuf<7,>=3.20 in /home/cloud/anaconda3/lib/python3.12/site-packages (from streamlit) (4.25.3)\n",
      "Collecting pyarrow>=7.0 (from streamlit)\n",
      "  Downloading pyarrow-23.0.0-cp312-cp312-manylinux_2_28_x86_64.whl.metadata (3.0 kB)\n",
      "Requirement already satisfied: requests<3,>=2.27 in /home/cloud/anaconda3/lib/python3.12/site-packages (from streamlit) (2.32.3)\n",
      "Collecting tenacity<10,>=8.1.0 (from streamlit)\n",
      "  Downloading tenacity-9.1.4-py3-none-any.whl.metadata (1.2 kB)\n",
      "Collecting toml<2,>=0.10.1 (from streamlit)\n",
      "  Downloading toml-0.10.2-py2.py3-none-any.whl.metadata (7.1 kB)\n",
      "Requirement already satisfied: tornado!=6.5.0,<7,>=6.0.3 in /home/cloud/anaconda3/lib/python3.12/site-packages (from streamlit) (6.4.1)\n",
      "Requirement already satisfied: typing-extensions<5,>=4.10.0 in /home/cloud/anaconda3/lib/python3.12/site-packages (from streamlit) (4.11.0)\n",
      "Requirement already satisfied: watchdog<7,>=2.1.5 in /home/cloud/anaconda3/lib/python3.12/site-packages (from streamlit) (4.0.1)\n",
      "Requirement already satisfied: jinja2 in /home/cloud/anaconda3/lib/python3.12/site-packages (from altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit) (3.1.4)\n",
      "Requirement already satisfied: jsonschema>=3.0 in /home/cloud/anaconda3/lib/python3.12/site-packages (from altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit) (4.23.0)\n",
      "Collecting narwhals>=1.27.1 (from altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit)\n",
      "  Downloading narwhals-2.16.0-py3-none-any.whl.metadata (14 kB)\n",
      "Collecting typing-extensions<5,>=4.10.0 (from streamlit)\n",
      "  Downloading typing_extensions-4.15.0-py3-none-any.whl.metadata (3.3 kB)\n",
      "Collecting gitdb<5,>=4.0.1 (from gitpython!=3.1.19,<4,>=3.0.7->streamlit)\n",
      "  Downloading gitdb-4.0.12-py3-none-any.whl.metadata (1.2 kB)\n",
      "Requirement already satisfied: python-dateutil>=2.8.2 in /home/cloud/anaconda3/lib/python3.12/site-packages (from pandas<3,>=1.4.0->streamlit) (2.9.0.post0)\n",
      "Requirement already satisfied: pytz>=2020.1 in /home/cloud/anaconda3/lib/python3.12/site-packages (from pandas<3,>=1.4.0->streamlit) (2024.1)\n",
      "Requirement already satisfied: tzdata>=2022.7 in /home/cloud/anaconda3/lib/python3.12/site-packages (from pandas<3,>=1.4.0->streamlit) (2023.3)\n",
      "Requirement already satisfied: charset-normalizer<4,>=2 in /home/cloud/anaconda3/lib/python3.12/site-packages (from requests<3,>=2.27->streamlit) (3.3.2)\n",
      "Requirement already satisfied: idna<4,>=2.5 in /home/cloud/anaconda3/lib/python3.12/site-packages (from requests<3,>=2.27->streamlit) (3.7)\n",
      "Requirement already satisfied: urllib3<3,>=1.21.1 in /home/cloud/anaconda3/lib/python3.12/site-packages (from requests<3,>=2.27->streamlit) (2.2.3)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in /home/cloud/anaconda3/lib/python3.12/site-packages (from requests<3,>=2.27->streamlit) (2024.12.14)\n",
      "Collecting smmap<6,>=3.0.1 (from gitdb<5,>=4.0.1->gitpython!=3.1.19,<4,>=3.0.7->streamlit)\n",
      "  Downloading smmap-5.0.2-py3-none-any.whl.metadata (4.3 kB)\n",
      "Requirement already satisfied: MarkupSafe>=2.0 in /home/cloud/anaconda3/lib/python3.12/site-packages (from jinja2->altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit) (2.1.3)\n",
      "Requirement already satisfied: attrs>=22.2.0 in /home/cloud/anaconda3/lib/python3.12/site-packages (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit) (23.1.0)\n",
      "Requirement already satisfied: jsonschema-specifications>=2023.03.6 in /home/cloud/anaconda3/lib/python3.12/site-packages (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit) (2023.7.1)\n",
      "Requirement already satisfied: referencing>=0.28.4 in /home/cloud/anaconda3/lib/python3.12/site-packages (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit) (0.30.2)\n",
      "Requirement already satisfied: rpds-py>=0.7.1 in /home/cloud/anaconda3/lib/python3.12/site-packages (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit) (0.10.6)\n",
      "Requirement already satisfied: six>=1.5 in /home/cloud/anaconda3/lib/python3.12/site-packages (from python-dateutil>=2.8.2->pandas<3,>=1.4.0->streamlit) (1.16.0)\n",
      "Downloading streamlit-1.54.0-py3-none-any.whl (9.1 MB)\n",
      "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m9.1/9.1 MB\u001b[0m \u001b[31m110.5 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
      "\u001b[?25hDownloading altair-6.0.0-py3-none-any.whl (795 kB)\n",
      "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m795.4/795.4 kB\u001b[0m \u001b[31m55.7 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
      "\u001b[?25hDownloading blinker-1.9.0-py3-none-any.whl (8.5 kB)\n",
      "Downloading cachetools-6.2.6-py3-none-any.whl (11 kB)\n",
      "Downloading gitpython-3.1.46-py3-none-any.whl (208 kB)\n",
      "Downloading pyarrow-23.0.0-cp312-cp312-manylinux_2_28_x86_64.whl (47.6 MB)\n",
      "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m47.6/47.6 MB\u001b[0m \u001b[31m153.5 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m00:01\u001b[0m\n",
      "\u001b[?25hDownloading pydeck-0.9.1-py2.py3-none-any.whl (6.9 MB)\n",
      "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m6.9/6.9 MB\u001b[0m \u001b[31m155.2 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
      "\u001b[?25hDownloading tenacity-9.1.4-py3-none-any.whl (28 kB)\n",
      "Downloading toml-0.10.2-py2.py3-none-any.whl (16 kB)\n",
      "Downloading typing_extensions-4.15.0-py3-none-any.whl (44 kB)\n",
      "Downloading gitdb-4.0.12-py3-none-any.whl (62 kB)\n",
      "Downloading narwhals-2.16.0-py3-none-any.whl (443 kB)\n",
      "Downloading smmap-5.0.2-py3-none-any.whl (24 kB)\n",
      "Installing collected packages: typing-extensions, toml, tenacity, smmap, pyarrow, narwhals, cachetools, blinker, pydeck, gitdb, gitpython, altair, streamlit\n",
      "  Attempting uninstall: typing-extensions\n",
      "    Found existing installation: typing_extensions 4.11.0\n",
      "    Uninstalling typing_extensions-4.11.0:\n",
      "      Successfully uninstalled typing_extensions-4.11.0\n",
      "Successfully installed altair-6.0.0 blinker-1.9.0 cachetools-6.2.6 gitdb-4.0.12 gitpython-3.1.46 narwhals-2.16.0 pyarrow-23.0.0 pydeck-0.9.1 smmap-5.0.2 streamlit-1.54.0 tenacity-9.1.4 toml-0.10.2 typing-extensions-4.15.0\n"
     ]
    }
   ],
   "source": [
    "!pip install streamlit"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "0e1e1173-00f4-4771-bda5-638a81da2ba6",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "import pickle"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "998f264d-913a-4350-be92-d5384904152b",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2026-02-15 03:21:24.255 WARNING streamlit.runtime.scriptrunner_utils.script_run_context: Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    }
   ],
   "source": [
    "st.set_page_config(page_title=\"Student Performance Prediction\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "c4ced9d1-28f4-4cc9-8035-f65a17324ae1",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2026-02-15 03:21:46.334 WARNING streamlit.runtime.scriptrunner_utils.script_run_context: Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:21:46.556 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run /home/cloud/anaconda3/lib/python3.12/site-packages/ipykernel_launcher.py [ARGUMENTS]\n",
      "2026-02-15 03:21:46.557 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:21:46.560 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:21:46.561 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:21:46.562 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:21:46.564 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    }
   ],
   "source": [
    "st.title(\"🎓 Student Performance Classification\")\n",
    "st.write(\"Predict whether a student will PASS or FAIL\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a37edf14-beaf-4b1b-b648-c8ca83e0df75",
   "metadata": {},
   "source": [
    "MODEL SELECTION DROPDOWN"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "3edb3c77-b343-4086-bacb-c40cc53182f5",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2026-02-15 03:22:48.023 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:22:48.024 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:22:48.026 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:22:48.027 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:22:48.028 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:22:48.031 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:22:48.032 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:22:48.033 Session state does not function when running a script without `streamlit run`\n",
      "2026-02-15 03:22:48.034 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:22:48.035 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:22:48.036 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    }
   ],
   "source": [
    "st.header(\"🤖 Select Machine Learning Model\")\n",
    "\n",
    "model_option = st.selectbox(\n",
    "    \"Choose a model\",\n",
    "    [\n",
    "        \"Logistic Regression\",\n",
    "        \"Decision Tree\",\n",
    "        \"K-Nearest Neighbors\",\n",
    "        \"Naive Bayes\",\n",
    "        \"Random Forest (Ensemble)\",\n",
    "        \"XGBoost (Ensemble)\"\n",
    "    ]\n",
    ")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "a7a4103d-6119-4889-a514-2e2a6a36af37",
   "metadata": {},
   "outputs": [],
   "source": [
    "model_paths = {\n",
    "    \"Logistic Regression\": \"model/logistic_regression.pkl\",\n",
    "    \"Decision Tree\": \"model/decision_tree.pkl\",\n",
    "    \"K-Nearest Neighbors\": \"model/knn.pkl\",\n",
    "    \"Naive Bayes\": \"model/naive_bayes.pkl\",\n",
    "    \"Random Forest (Ensemble)\": \"model/random_forest.pkl\",\n",
    "    \"XGBoost (Ensemble)\": \"model/xgboost.pkl\"\n",
    "}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "f09c803a-7c40-4d38-923d-e0ce5b654637",
   "metadata": {},
   "outputs": [],
   "source": [
    "model = pickle.load(open(model_paths[model_option], \"rb\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "9fa7d83f-5278-4275-836e-d3533c4034d3",
   "metadata": {},
   "outputs": [],
   "source": [
    "scaler = pickle.load(open(\"model/scaler.pkl\", \"rb\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "c0e599ed-0883-47e6-8d4c-bacc71e2f1c6",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2026-02-15 03:23:58.333 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.335 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.336 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.337 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.337 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.338 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.339 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.341 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.341 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.342 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.343 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.344 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.344 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.345 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.346 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.346 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.347 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.348 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.348 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.349 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.350 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.351 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.352 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.353 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.353 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.354 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.355 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.355 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.356 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.356 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.357 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.361 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.361 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.362 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.364 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.365 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.366 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.367 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.367 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.370 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.371 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.371 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.372 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.373 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.373 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.374 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.374 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.375 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.377 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.378 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.379 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.380 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.381 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.381 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.382 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.387 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.388 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.389 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.391 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.392 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.392 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.393 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.394 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.395 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.395 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.396 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.397 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.399 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.400 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.401 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.402 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.404 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.404 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.405 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.406 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.407 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.408 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.409 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.410 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.411 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.411 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.412 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.413 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.413 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.414 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.416 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.417 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.418 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.418 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.419 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.420 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.421 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.422 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.423 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.423 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.424 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.425 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.425 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.427 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.428 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.429 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.429 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.430 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.431 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.432 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.433 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.433 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.437 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.437 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.438 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.439 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.439 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.440 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.441 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.441 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.442 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.443 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.444 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.444 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.447 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.447 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.448 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.450 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.450 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.451 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.452 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.452 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.453 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.454 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.454 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.455 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.456 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.456 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.457 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.458 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.458 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.459 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.460 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.461 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.462 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.463 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.464 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.464 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.465 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.466 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.467 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.468 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.469 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.469 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.470 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.471 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:23:58.471 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    }
   ],
   "source": [
    "st.header(\"📋 Enter Student Details\")\n",
    "\n",
    "school = st.selectbox(\"School\", [\"GP\", \"MS\"])\n",
    "sex = st.selectbox(\"Sex\", [\"F\", \"M\"])\n",
    "age = st.slider(\"Age\", 15, 22, 17)\n",
    "address = st.selectbox(\"Address\", [\"U\", \"R\"])\n",
    "famsize = st.selectbox(\"Family Size\", [\"LE3\", \"GT3\"])\n",
    "Pstatus = st.selectbox(\"Parent Status\", [\"T\", \"A\"])\n",
    "\n",
    "Medu = st.slider(\"Mother Education (0-4)\", 0, 4, 2)\n",
    "Fedu = st.slider(\"Father Education (0-4)\", 0, 4, 2)\n",
    "\n",
    "studytime = st.slider(\"Study Time (1-4)\", 1, 4, 2)\n",
    "failures = st.slider(\"Past Failures (0-4)\", 0, 4, 0)\n",
    "\n",
    "schoolsup = st.selectbox(\"School Support\", [\"yes\", \"no\"])\n",
    "famsup = st.selectbox(\"Family Support\", [\"yes\", \"no\"])\n",
    "paid = st.selectbox(\"Extra Paid Classes\", [\"yes\", \"no\"])\n",
    "activities = st.selectbox(\"Extra Activities\", [\"yes\", \"no\"])\n",
    "internet = st.selectbox(\"Internet Access\", [\"yes\", \"no\"])\n",
    "romantic = st.selectbox(\"Romantic Relationship\", [\"yes\", \"no\"])\n",
    "\n",
    "famrel = st.slider(\"Family Relationship (1-5)\", 1, 5, 3)\n",
    "freetime = st.slider(\"Free Time (1-5)\", 1, 5, 3)\n",
    "goout = st.slider(\"Going Out (1-5)\", 1, 5, 3)\n",
    "Dalc = st.slider(\"Workday Alcohol (1-5)\", 1, 5, 1)\n",
    "Walc = st.slider(\"Weekend Alcohol (1-5)\", 1, 5, 2)\n",
    "health = st.slider(\"Health Status (1-5)\", 1, 5, 3)\n",
    "absences = st.slider(\"Absences\", 0, 100, 5)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "66582974-9b5d-470d-9d15-5c6b831972aa",
   "metadata": {},
   "source": [
    "PREDICTION"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "2e7caf22-5172-4116-b4ff-3292587db067",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2026-02-15 03:27:08.653 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:27:08.656 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:27:08.658 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:27:08.660 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:27:08.660 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-15 03:27:08.662 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    }
   ],
   "source": [
    "if st.button(\"🔍 Predict Performance\"):\n",
    "\n",
    "    input_dict = {\n",
    "        \"school\": school,\n",
    "        \"sex\": sex,\n",
    "        \"age\": age,\n",
    "        \"address\": address,\n",
    "        \"famsize\": famsize,\n",
    "        \"Pstatus\": Pstatus,\n",
    "        \"Medu\": Medu,\n",
    "        \"Fedu\": Fedu,\n",
    "        \"studytime\": studytime,\n",
    "        \"failures\": failures,\n",
    "        \"schoolsup\": schoolsup,\n",
    "        \"famsup\": famsup,\n",
    "        \"paid\": paid,\n",
    "        \"activities\": activities,\n",
    "        \"internet\": internet,\n",
    "        \"romantic\": romantic,\n",
    "        \"famrel\": famrel,\n",
    "        \"freetime\": freetime,\n",
    "        \"goout\": goout,\n",
    "        \"Dalc\": Dalc,\n",
    "        \"Walc\": Walc,\n",
    "        \"health\": health,\n",
    "        \"absences\": absences\n",
    "    }\n",
    "\n",
    "    \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "4d7dcd4e-f652-4f4c-b9cb-36c634e04581",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'input_dict' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[0;32mIn[30], line 1\u001b[0m\n\u001b[0;32m----> 1\u001b[0m input_df \u001b[38;5;241m=\u001b[39m pd\u001b[38;5;241m.\u001b[39mDataFrame([input_dict])\n",
      "\u001b[0;31mNameError\u001b[0m: name 'input_dict' is not defined"
     ]
    }
   ],
   "source": [
    "input_df = pd.DataFrame([input_dict])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "152e7bb6-6dfe-447c-aa87-5505207b362e",
   "metadata": {},
   "outputs": [
    {
     "ename": "IndentationError",
     "evalue": "unexpected indent (2573293282.py, line 2)",
     "output_type": "error",
     "traceback": [
      "\u001b[0;36m  Cell \u001b[0;32mIn[26], line 2\u001b[0;36m\u001b[0m\n\u001b[0;31m    input_df.replace(binary_map, inplace=True)\u001b[0m\n\u001b[0m    ^\u001b[0m\n\u001b[0;31mIndentationError\u001b[0m\u001b[0;31m:\u001b[0m unexpected indent\n"
     ]
    }
   ],
   "source": [
    "binary_map = {\"yes\": 1, \"no\": 0}\n",
    "    input_df.replace(binary_map, inplace=True)\n",
    "\n",
    "    categorical_map = {\n",
    "        \"school\": {\"GP\": 0, \"MS\": 1},\n",
    "        \"sex\": {\"F\": 0, \"M\": 1},\n",
    "        \"address\": {\"U\": 0, \"R\": 1},\n",
    "        \"famsize\": {\"LE3\": 0, \"GT3\": 1},\n",
    "        \"Pstatus\": {\"T\": 0, \"A\": 1},\n",
    "    }"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "71e5e843-7dcf-4737-90da-2c0dfce79016",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

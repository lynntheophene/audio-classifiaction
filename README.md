# audio-classifiaction



This is a simple language classifier model built for the **Rodia dataset**.

---

## 🛠️ Environment Setup

You can use either `venv` or `conda` to create your virtual environment.

### Option 1: Using `venv`

> Recommended Python version: **below 3.12** (e.g., Python 3.10) for TensorFlow compatibility.

```bash
python3.10 -m venv rodia_env
source rodia_env/bin/activate         # On Windows: rodia_env\Scripts\activate
```

### Option 2: Using `conda`

```bash
conda create -n rodia_env python=3.10
conda activate rodia_env
```

---

## 📦 Install Required Libraries

Run the following script to install all dependencies:

```bash
python import_installer.py
```

---

## 📁 Dataset Structure

The dataset is organized as follows:

| Directory             | Labels                  |
|-----------------------|--------------------------|
| `real_data/data/train` | Ard, Ban, Mol, Mun, Olt |
| `real_data/data/test1` | Ard, Ban, Mol, Mun, Olt |

Each label folder contains sample data for that dialect or language.

---

## 📬 Contact

For any queries or support, feel free to reach out:  
**lynntheophene@gmail.com**

---

Feel free to fork this repo and experiment with the model or dataset. Contributions are welcome!



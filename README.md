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
## 📚 Dataset Citation

This project utilizes the **RoDia dataset** for Romanian dialect identification from speech.

> **Citation**:
>
> Codruț Rotaru, Nicolae Cătălin Ristea, and Radu Tudor Ionescu. 2024. *RoDia: A New Dataset for Romanian Dialect Identification from Speech*. In *Findings of the Association for Computational Linguistics: NAACL 2024*, pages 279–286, Mexico City, Mexico. Association for Computational Linguistics. [https://aclanthology.org/2024.findings-naacl.20/](https://aclanthology.org/2024.findings-naacl.20/)

🔗 **Dataset Repository**: [https://github.com/codrut2/RoDia](https://github.com/codrut2/RoDia)

📄 **License**: Refer to the dataset repository for licensing information.

Please ensure that you adhere to the licensing terms specified in the dataset's repository.




---

Feel free to fork this repo and experiment with the model . Contributions are welcome!



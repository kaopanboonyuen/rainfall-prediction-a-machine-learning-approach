# Advanced Machine Learning Techniques for Accurate Rainfall Prediction

Welcome to the repository for **"Advanced Machine Learning Techniques for Accurate Rainfall Prediction"**. This project, developed by Teerapong Panboonyuen (Kao Panboonyuen), focuses on leveraging state-of-the-art machine learning models to enhance the accuracy of rainfall predictions.

## Our Recent Publication

We are pleased to share our recent publication: **"A Performance Comparison between GIS-based and Neuron Network Methods for Flood Susceptibility Assessment in Ayutthaya Province"**. You can access the full paper [here](https://tis.wu.ac.th/index.php/tis/article/view/2038).

![](paper_result.png)

### Abstract

Flooding has been a longstanding issue in Thailand. Due to its geographical setup, mitigation and management of floods are challenging and hard to execute. One of the tools used in managing these events is “flood susceptibility mapping,” which estimates incident probabilities and plans rescue paths.

To create such maps, the traditional GIS method called FRAM (Flood Risk Assessment Model), combined with AHP (Analytical Hierarchy Process), is used and implemented on ArcGIS software. In this method, we first created a comparison table to compute weights for each of the selected factors. Then, these weights were used in the FRAM model within ArcGIS to create a flood susceptibility map for each region, classifying areas into five risk levels: very high, high, medium, low, and very low.

In contrast, the field of computer science has seen a rise in the adoption of machine learning and AI across various domains, promising enhanced effectiveness. In this work, we applied an Artificial Neural Network (ANN) to create the flood susceptibility map, classifying areas as either flood-prone or flood-free. This study compares the traditional GIS-based method with the ANN approach, using data from Thailand’s Ayutthaya Province as a case study to evaluate flood-prone areas.

Both methods used six selected factors from the literature: (i) flow accumulation, (ii) elevation, (iii) land use, (iv) rainfall intensity, (v) slope, and (vi) soil types. The results were verified with historical flood data and compared. Our findings indicate that ANN outperformed the FRAM method, achieving a precision of 79.90%, recall of 79.04%, F1-score of 79.08%, and accuracy of 79.31%. Furthermore, sensitivity analysis revealed that only three factors—flow accumulation, elevation, and soil types—were crucial in predicting flood susceptibility. Thus, this simplified methodology could be applied to other regions where similar assessments are required.

### Citation

If you use our work, please cite it using the following BibTeX entry:

```bibtex
@article{vajeethaveesin2022performance,
  title={A performance comparison between GIS-based and neuron network methods for flood susceptibility assessment in ayutthaya province},
  author={Vajeethaveesin, Thanat and Panboonyuen, Teerapong},
  journal={Trends in Sciences},
  volume={19},
  number={2},
  pages={2038--2038},
  year={2022}
}
```

## Overview

Accurate rainfall prediction is crucial for various sectors, including agriculture, water resource management, and disaster preparedness. This project explores a range of machine learning algorithms to improve the precision and reliability of rainfall forecasts. By comparing traditional methods with advanced models, this work aims to demonstrate the potential of machine learning in meteorological applications.

## Features

- **Data Preprocessing**: Handling missing data, normalization, and feature engineering.
- **Model Implementation**: Includes implementations of various machine learning models such as Random Forest, Gradient Boosting, and Neural Networks.
- **Evaluation**: Rigorous performance evaluation using metrics like RMSE, MAE, and R².
- **Visualization**: Graphical representation of results for better interpretation and analysis.

## Installation

Clone this repository to your local machine:

```bash
git clone https://github.com/kaopanboonyuen/rainfall-prediction-a-machine-learning-approach.git
cd rainfall-prediction-a-machine-learning-approach
```

Install the required Python packages:

```bash
pip install -r requirements.txt
```

## Usage

To start using the models and scripts, follow these steps:

1. **Data Preparation**: Place your dataset in the `data/` directory.
2. **Run the Model**: Execute the script for the desired model:
   ```bash
   python run_model.py --model random_forest
   ```
3. **Analyze Results**: View the output metrics and plots in the `results/` directory.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Contact

For any inquiries or discussions, you can reach out to Teerapong Panboonyuen (Kao Panboonyuen) through GitHub.

## Acknowledgments

Special thanks to all collaborators and contributors who helped make this project possible.

---

[View the Repository](https://github.com/kaopanboonyuen/rainfall-prediction-a-machine-learning-approach)
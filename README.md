# Advanced Machine Learning Techniques for Accurate Rainfall Prediction

## Authors
Teerapong Panboonyuen (also known as Kao Panboonyuen)

## Overview
This repository contains the implementation of advanced machine learning techniques for accurate rainfall prediction. The project explores various machine learning models, including Random Forest, Gradient Boosting, and Neural Networks, to develop a predictive model for rainfall using relevant features from the dataset.

![](paper_result.png)

## Dataset
**Note:** You must have permission from Geo-Informatics and Space Technology Development Agency (GISTDA Thailand) to access the dataset used in this project. The dataset is not provided in this repository due to its private nature.

## Publication
Our research is published in the following paper:

- **Title:** A Performance Comparison between GIS-based and Neuron Network Methods for Flood Susceptibility Assessment in Ayutthaya Province
- **Authors:** Thanat Vajeethaveesin, Teerapong Panboonyuen
- **Journal:** Trends in Sciences, Volume 19, Number 2, Pages 2038-2038, Year 2022
- **Link:** [A Performance Comparison between GIS-based and Neuron Network Methods for Flood Susceptibility Assessment in Ayutthaya Province](https://tis.wu.ac.th/index.php/tis/article/view/2038)

### Abstract
Flooding has been a long-standing issue in Thailand. Due to its geographical setup, mitigation and management of floods are challenging and hard to execute. One of the tools used in managing the events is “flood susceptibility mapping,” in which an incident probability as well as a rescue path is estimated and planned. 

To create one, the traditional GIS method called FRAM (flood risk assessment model), combined with AHP (analytical hierarchy process), is used and implemented on ArcGIS software. In this method, we first created a comparison table to compute weights for each of the selected factors. Then the computed weights were used in the FRAM model in ArcGIS to create a flood susceptibility map for each region. Each region was then classified as very high, high, medium, low, and very low risk. 

On the other hand, in computer science, machine learning and AI are prevalent and being adopted in various domains, promising the effectiveness of the method, potentially beating the aforementioned traditional method. Therefore, ANN (artificial neural network) is adopted in this work to create the flood susceptibility map. The ANN technique is developed by using causal factors. The ANN classifies areas as either flood areas or flood-free areas.

The two methods from different disciplines (GIS and Computer Science) are applied and described in this paper with the intention to prove whether machine learning is really efficient and can outperform the traditional GIS approach. Data on Thailand’s Ayutthaya Province is used in this work as a case study - in order to assess flood-prone areas and compare for performance evaluation. 

Both of which use the 6 selected factors according to the literature: (i) flow accumulation, (ii) elevation, (iii) land use, (iv) rainfall intensity, (v) slope, and (vi) soil types. The results from the two methods were verified with historical flood data and compared. The results showed that ANN (obtained via sensitivity analysis) outperformed the FRAM with a precision of 79.90 %, recall of 79.04 %, F1-score of 79.08 %, and accuracy of 79.31 %. 

In addition, we found that (according to our ANN experiments) the main causal factors related to the flood susceptibility map only included 3 factors: flow accumulation, elevation, and soil types. Therefore, the proposed methodology for the assessment of flood susceptibility areas using these 3 factors could be considered sufficient and applied to other regions in related applications when needed.

### Citation (BibTeX)
```bibtex
@article{vajeethaveesin2022performance,
  title={A performance comparison between GIS-based and neuron network methods for flood susceptibility assessment in Ayutthaya Province},
  author={Vajeethaveesin, Thanat and Panboonyuen, Teerapong},
  journal={Trends in Sciences},
  volume={19},
  number={2},
  pages={2038--2038},
  year={2022}
}
```

## Getting Started
To run the models in this project, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/kaopanboonyuen/rainfall-prediction-a-machine-learning-approach.git
   cd rainfall-prediction-a-machine-learning-approach
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the model:**
   Since the dataset is private, you need to obtain it yourself. Once you have access, you can use the `run_model.py` script to train and evaluate the models:
   ```bash
   python run_model.py
   ```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
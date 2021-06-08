{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "import seaborn as sns\n",
    "import matplotlib.pyplot as plt\n",
    "%matplotlib inline\n",
    "import warnings \n",
    "warnings.filterwarnings('ignore')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.read_csv('train.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>battery_power</th>\n",
       "      <th>blue</th>\n",
       "      <th>clock_speed</th>\n",
       "      <th>dual_sim</th>\n",
       "      <th>fc</th>\n",
       "      <th>four_g</th>\n",
       "      <th>int_memory</th>\n",
       "      <th>m_dep</th>\n",
       "      <th>mobile_wt</th>\n",
       "      <th>n_cores</th>\n",
       "      <th>...</th>\n",
       "      <th>px_height</th>\n",
       "      <th>px_width</th>\n",
       "      <th>ram</th>\n",
       "      <th>sc_h</th>\n",
       "      <th>sc_w</th>\n",
       "      <th>talk_time</th>\n",
       "      <th>three_g</th>\n",
       "      <th>touch_screen</th>\n",
       "      <th>wifi</th>\n",
       "      <th>price_range</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>842</td>\n",
       "      <td>0</td>\n",
       "      <td>2.2</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>7</td>\n",
       "      <td>0.6</td>\n",
       "      <td>188</td>\n",
       "      <td>2</td>\n",
       "      <td>...</td>\n",
       "      <td>20</td>\n",
       "      <td>756</td>\n",
       "      <td>2549</td>\n",
       "      <td>9</td>\n",
       "      <td>7</td>\n",
       "      <td>19</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1021</td>\n",
       "      <td>1</td>\n",
       "      <td>0.5</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>53</td>\n",
       "      <td>0.7</td>\n",
       "      <td>136</td>\n",
       "      <td>3</td>\n",
       "      <td>...</td>\n",
       "      <td>905</td>\n",
       "      <td>1988</td>\n",
       "      <td>2631</td>\n",
       "      <td>17</td>\n",
       "      <td>3</td>\n",
       "      <td>7</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>563</td>\n",
       "      <td>1</td>\n",
       "      <td>0.5</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>41</td>\n",
       "      <td>0.9</td>\n",
       "      <td>145</td>\n",
       "      <td>5</td>\n",
       "      <td>...</td>\n",
       "      <td>1263</td>\n",
       "      <td>1716</td>\n",
       "      <td>2603</td>\n",
       "      <td>11</td>\n",
       "      <td>2</td>\n",
       "      <td>9</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>615</td>\n",
       "      <td>1</td>\n",
       "      <td>2.5</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>10</td>\n",
       "      <td>0.8</td>\n",
       "      <td>131</td>\n",
       "      <td>6</td>\n",
       "      <td>...</td>\n",
       "      <td>1216</td>\n",
       "      <td>1786</td>\n",
       "      <td>2769</td>\n",
       "      <td>16</td>\n",
       "      <td>8</td>\n",
       "      <td>11</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1821</td>\n",
       "      <td>1</td>\n",
       "      <td>1.2</td>\n",
       "      <td>0</td>\n",
       "      <td>13</td>\n",
       "      <td>1</td>\n",
       "      <td>44</td>\n",
       "      <td>0.6</td>\n",
       "      <td>141</td>\n",
       "      <td>2</td>\n",
       "      <td>...</td>\n",
       "      <td>1208</td>\n",
       "      <td>1212</td>\n",
       "      <td>1411</td>\n",
       "      <td>8</td>\n",
       "      <td>2</td>\n",
       "      <td>15</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>5 rows × 21 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "   battery_power  blue  clock_speed  dual_sim  fc  four_g  int_memory  m_dep  \\\n",
       "0            842     0          2.2         0   1       0           7    0.6   \n",
       "1           1021     1          0.5         1   0       1          53    0.7   \n",
       "2            563     1          0.5         1   2       1          41    0.9   \n",
       "3            615     1          2.5         0   0       0          10    0.8   \n",
       "4           1821     1          1.2         0  13       1          44    0.6   \n",
       "\n",
       "   mobile_wt  n_cores  ...  px_height  px_width   ram  sc_h  sc_w  talk_time  \\\n",
       "0        188        2  ...         20       756  2549     9     7         19   \n",
       "1        136        3  ...        905      1988  2631    17     3          7   \n",
       "2        145        5  ...       1263      1716  2603    11     2          9   \n",
       "3        131        6  ...       1216      1786  2769    16     8         11   \n",
       "4        141        2  ...       1208      1212  1411     8     2         15   \n",
       "\n",
       "   three_g  touch_screen  wifi  price_range  \n",
       "0        0             0     1            1  \n",
       "1        1             1     0            2  \n",
       "2        1             1     0            2  \n",
       "3        1             0     0            2  \n",
       "4        1             1     0            1  \n",
       "\n",
       "[5 rows x 21 columns]"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "battery_power    0\n",
       "blue             0\n",
       "clock_speed      0\n",
       "dual_sim         0\n",
       "fc               0\n",
       "four_g           0\n",
       "int_memory       0\n",
       "m_dep            0\n",
       "mobile_wt        0\n",
       "n_cores          0\n",
       "pc               0\n",
       "px_height        0\n",
       "px_width         0\n",
       "ram              0\n",
       "sc_h             0\n",
       "sc_w             0\n",
       "talk_time        0\n",
       "three_g          0\n",
       "touch_screen     0\n",
       "wifi             0\n",
       "price_range      0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 2000 entries, 0 to 1999\n",
      "Data columns (total 21 columns):\n",
      " #   Column         Non-Null Count  Dtype  \n",
      "---  ------         --------------  -----  \n",
      " 0   battery_power  2000 non-null   int64  \n",
      " 1   blue           2000 non-null   int64  \n",
      " 2   clock_speed    2000 non-null   float64\n",
      " 3   dual_sim       2000 non-null   int64  \n",
      " 4   fc             2000 non-null   int64  \n",
      " 5   four_g         2000 non-null   int64  \n",
      " 6   int_memory     2000 non-null   int64  \n",
      " 7   m_dep          2000 non-null   float64\n",
      " 8   mobile_wt      2000 non-null   int64  \n",
      " 9   n_cores        2000 non-null   int64  \n",
      " 10  pc             2000 non-null   int64  \n",
      " 11  px_height      2000 non-null   int64  \n",
      " 12  px_width       2000 non-null   int64  \n",
      " 13  ram            2000 non-null   int64  \n",
      " 14  sc_h           2000 non-null   int64  \n",
      " 15  sc_w           2000 non-null   int64  \n",
      " 16  talk_time      2000 non-null   int64  \n",
      " 17  three_g        2000 non-null   int64  \n",
      " 18  touch_screen   2000 non-null   int64  \n",
      " 19  wifi           2000 non-null   int64  \n",
      " 20  price_range    2000 non-null   int64  \n",
      "dtypes: float64(2), int64(19)\n",
      "memory usage: 328.2 KB\n"
     ]
    }
   ],
   "source": [
    "df.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.distplot(df['battery_power']);"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1238.5185"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['battery_power'].mean()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.countplot(df['blue'])\n",
    "plt.show()\n",
    "plt.pie(x=df['blue'].value_counts(),labels =(['No','Yes']),radius=2,colors=['m','c'],autopct='%.1f',pctdistance=0.9,explode=(0, 0.02));\n",
    "plt.pie([1],colors='w',radius=1);"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.countplot(df['dual_sim']);\n",
    "plt.show()\n",
    "df['dual_sim'].value_counts()\n",
    "plt.pie(x=df['dual_sim'].value_counts(),labels=['Yes','No'],radius=2,colors=['m','c'],autopct='%.2f',pctdistance=0.9,explode=(0, 0.03));\n",
    "plt.pie([1],colors='w',radius=1);"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='fc', ylabel='count'>"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.countplot(df['fc'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAYsAAAEHCAYAAABfkmooAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjMuMiwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8vihELAAAACXBIWXMAAAsTAAALEwEAmpwYAAASnUlEQVR4nO3df6zdd33f8ecLBwwUsiTKTeraZnZbl81Ju0HuslCmCTVd46oURy2ZHC3DQCSvNOtgP1rstVr2Q5YitaMFSpA8SOKsNK5Ff8SrRFvXG0NtA9kN0CVO6sY0NL6NiS+kKyGjLvbe++N8o544597PyeWec65zng/p6Ps97+/n+/2+jey8+P48qSokSVrKSybdgCRp9TMsJElNhoUkqcmwkCQ1GRaSpKYLJt3AqFx66aW1adOmSbchSeeVBx544MtVNXNu/UUbFps2bWJubm7SbUjSeSXJnw6qexpKktRkWEiSmgwLSVKTYSFJajIsJElNhoUkqcmwkCQ1GRaSpCbDQpLU9KJ9glt6MXv8P373pFvQKvSaf/fgyLbtkYUkqcmwkCQ1GRaSpCbDQpLUZFhIkpoMC0lSk2EhSWoyLCRJTYaFJKnJsJAkNRkWkqQmw0KS1DSysEhyR5JTSR4asOzfJKkkl/bV9iQ5nuRYkuv66lclebBb9oEkGVXPkqTBRnlkcRew7dxiko3APwIe76ttBXYAV3Tr3J5kTbf4w8AuYEv3ed42JUmjNbKwqKpPAU8NWPTzwE8B1VfbDhyoqtNV9RhwHLg6yTrgwqq6r6oKuBu4flQ9S5IGG+s1iyRvAf6sqv7wnEXrgRN93+e72vpu/ty6JGmMxvbjR0leCfw08AODFg+o1RL1xfaxi94pK17zmtcso0tJ0iDjPLL4DmAz8IdJvghsAD6b5FvpHTFs7Bu7AXiiq28YUB+oqvZV1WxVzc7MzKxw+5I0vcYWFlX1YFVdVlWbqmoTvSB4fVV9CTgE7EiyNslmehey76+qk8DTSa7p7oJ6G3DvuHqWJPWM8tbZe4D7gNcmmU9y82Jjq+oocBB4GPgt4JaqOtstfhfwEXoXvb8AfGJUPUuSBhvZNYuqurGxfNM53/cCeweMmwOuXNHmJEkviE9wS5KaDAtJUpNhIUlqMiwkSU2GhSSpybCQJDUZFpKkJsNCktRkWEiSmgwLSVKTYSFJajIsJElNhoUkqcmwkCQ1GRaSpCbDQpLUZFhIkpoMC0lS0yh/g/uOJKeSPNRX+9kkf5Tkfyf59SQX9S3bk+R4kmNJruurX5XkwW7ZB5JkVD1LkgYb5ZHFXcC2c2qHgSur6nuAPwb2ACTZCuwArujWuT3Jmm6dDwO7gC3d59xtSpJGbGRhUVWfAp46p/Y7VXWm+/ppYEM3vx04UFWnq+ox4DhwdZJ1wIVVdV9VFXA3cP2oepYkDTbJaxbvBD7Rza8HTvQtm+9q67v5c+uSpDGaSFgk+WngDPCxZ0sDhtUS9cW2uyvJXJK5hYWFb75RSRIwgbBIshN4M/BPulNL0Dti2Ng3bAPwRFffMKA+UFXtq6rZqpqdmZlZ2cYlaYqNNSySbAPeC7ylqv5v36JDwI4ka5Nspnch+/6qOgk8neSa7i6otwH3jrNnSRJcMKoNJ7kHeBNwaZJ54FZ6dz+tBQ53d8B+uqp+rKqOJjkIPEzv9NQtVXW229S76N1Z9Qp61zg+gSRprEYWFlV144DyR5cYvxfYO6A+B1y5gq1Jkl4gn+CWJDUZFpKkJsNCktRkWEiSmgwLSVKTYSFJajIsJElNhoUkqcmwkCQ1GRaSpCbDQpLUZFhIkpoMC0lSk2EhSWoyLCRJTYaFJKnJsJAkNRkWkqQmw0KS1DSysEhyR5JTSR7qq12S5HCSR7vpxX3L9iQ5nuRYkuv66lclebBb9oEkGVXPkqTBRnlkcRew7ZzabuBIVW0BjnTfSbIV2AFc0a1ze5I13TofBnYBW7rPuduUJI3YyMKiqj4FPHVOeTuwv5vfD1zfVz9QVaer6jHgOHB1knXAhVV1X1UVcHffOpKkMRn3NYvLq+okQDe9rKuvB070jZvvauu7+XPrAyXZlWQuydzCwsKKNi5J02y1XOAedB2ilqgPVFX7qmq2qmZnZmZWrDlJmnbjDosnu1NLdNNTXX0e2Ng3bgPwRFffMKAuSRqjcYfFIWBnN78TuLevviPJ2iSb6V3Ivr87VfV0kmu6u6De1reOJGlMLhjVhpPcA7wJuDTJPHArcBtwMMnNwOPADQBVdTTJQeBh4AxwS1Wd7Tb1Lnp3Vr0C+ET3kSSN0cjCoqpuXGTRtYuM3wvsHVCfA65cwdYkSS/QarnALUlaxQwLSVKTYSFJajIsJElNhoUkqcmwkCQ1GRaSpCbDQpLUZFhIkpoMC0lS01BhkeTIMDVJ0ovTku+GSvJy4JX0XgZ4MX/9+xIXAt824t4kSatE60WC/wx4D71geIC/DouvAh8aXVuSpNVkybCoqvcD70/yE1X1wTH1JElaZYZ6RXlVfTDJ9wKb+tepqrtH1JckaRUZKiyS/FfgO4DPA8/+KFEBhoUkTYFhf/xoFthaVTXKZiRJq9Owz1k8BHzrKBuRJK1ew4bFpcDDSX47yaFnP8vdaZJ/meRokoeS3JPk5UkuSXI4yaPd9OK+8XuSHE9yLMl1y92vJGl5hj0N9e9XaodJ1gP/gt5pra8nOQjsALYCR6rqtiS7gd3Ae5Ns7ZZfQe8W3t9N8l1VdXaRXUiSVtiwd0P9zxHs9xVJvkHvob8ngD3Am7rl+4FPAu8FtgMHquo08FiS48DVwH0r3JMkaRHDvu7j6SRf7T5/meRskq8uZ4dV9WfAzwGPAyeBv6iq3wEur6qT3ZiTwGXdKuuBE32bmO9qg/rclWQuydzCwsJy2pMkDTBUWFTVq6vqwu7zcuBHgV9czg67axHbgc30Tit9S5KbllplUEuL9LmvqmaranZmZmY57UmSBljWW2er6jeA71vmPr8feKyqFqrqG8CvAd8LPJlkHUA3PdWNnwc29q2/gd5pK0nSmAz7UN6P9H19Cb3nLpb7zMXjwDVJXgl8HbgWmAOeAXYCt3XTe7vxh4BfTvI+ekciW4D7l7lvSdIyDHs31A/3zZ8BvkjvVNILVlWfSfJx4LPdtj4H7ANeBRxMcjO9QLmhG3+0u2Pq4W78Ld4JJUnjNezdUO9YyZ1W1a3AreeUT9M7yhg0fi+wdyV7kCQNb9i7oTYk+fUkp5I8meRXk2wYdXOSpNVh2Avcd9K7dvBt9G5b/W9dTZI0BYYNi5mqurOqznSfuwDvTZWkKTFsWHw5yU1J1nSfm4CvjLIxSdLqMWxYvBP4x8CX6D11/VZgRS96S5JWr2Fvnf1PwM6q+nOAJJfQe2XHO0fVmCRp9Rj2yOJ7ng0KgKp6CnjdaFqSJK02w4bFS875fYlLGP6oRJJ0nhv2P/j/GfiD7snronf9wofkJGlKDPsE991J5ui9PDDAj1TVwyPtTJK0agx9KqkLBwNCkqbQsl5RLkmaLoaFJKnJsJAkNRkWkqQmw0KS1GRYSJKaDAtJUtNEwiLJRUk+nuSPkjyS5A1JLklyOMmj3bT/9SJ7khxPcizJdZPoWZKm2aSOLN4P/FZV/S3g7wCPALuBI1W1BTjSfSfJVmAHcAWwDbg9yZqJdC1JU2rsYZHkQuAfAh8FqKq/qqr/A2wH9nfD9gPXd/PbgQNVdbqqHgOOA1ePs2dJmnaTOLL4dmABuDPJ55J8JMm3AJdX1UmAbnpZN349cKJv/fmu9jxJdiWZSzK3sLAwuj+BJE2ZSYTFBcDrgQ9X1euAZ+hOOS0iA2o1aGBV7auq2aqanZnxJ8IlaaVMIizmgfmq+kz3/eP0wuPJJOsAuumpvvEb+9bfADwxpl4lSUwgLKrqS8CJJK/tStfSe5vtIWBnV9sJ3NvNHwJ2JFmbZDOwBbh/jC1L0tSb1K/d/QTwsSQvA/4EeAe94DqY5GbgceAGgKo6muQgvUA5A9xSVWcn07YkTaeJhEVVfR6YHbDo2kXG78Vf5pOkifEJbklSk2EhSWoyLCRJTYaFJKnJsJAkNRkWkqQmw0KS1GRYSJKaDAtJUpNhIUlqMiwkSU2TepHgqnfVT9496Ra0Cj3ws2+bdAvSRHhkIUlqMiwkSU2GhSSpybCQJDUZFpKkJsNCktQ0sbBIsibJ55L8Zvf9kiSHkzzaTS/uG7snyfEkx5JcN6meJWlaTfLI4t3AI33fdwNHqmoLcKT7TpKtwA7gCmAbcHuSNWPuVZKm2kTCIskG4IeAj/SVtwP7u/n9wPV99QNVdbqqHgOOA1ePqVVJEpM7svgF4KeA/9dXu7yqTgJ008u6+nrgRN+4+a4mSRqTsYdFkjcDp6rqgWFXGVCrRba9K8lckrmFhYVl9yhJeq5JHFm8EXhLki8CB4DvS/JLwJNJ1gF001Pd+HlgY9/6G4AnBm24qvZV1WxVzc7MzIyqf0maOmMPi6raU1UbqmoTvQvX/72qbgIOATu7YTuBe7v5Q8COJGuTbAa2APePuW1Jmmqr6a2ztwEHk9wMPA7cAFBVR5McBB4GzgC3VNXZybUpSdNnomFRVZ8EPtnNfwW4dpFxe4G9Y2tMkvQcPsEtSWoyLCRJTYaFJKnJsJAkNRkWkqQmw0KS1GRYSJKaDAtJUpNhIUlqMiwkSU2GhSSpybCQJDUZFpKkJsNCktRkWEiSmgwLSVKTYSFJajIsJElNYw+LJBuT/I8kjyQ5muTdXf2SJIeTPNpNL+5bZ0+S40mOJblu3D1L0rSbxJHFGeBfV9XfBq4BbkmyFdgNHKmqLcCR7jvdsh3AFcA24PYkaybQtyRNrbGHRVWdrKrPdvNPA48A64HtwP5u2H7g+m5+O3Cgqk5X1WPAceDqsTYtSVNuotcskmwCXgd8Bri8qk5CL1CAy7ph64ETfavNdzVJ0phMLCySvAr4VeA9VfXVpYYOqNUi29yVZC7J3MLCwkq0KUliQmGR5KX0guJjVfVrXfnJJOu65euAU119HtjYt/oG4IlB262qfVU1W1WzMzMzo2lekqbQJO6GCvBR4JGqel/fokPAzm5+J3BvX31HkrVJNgNbgPvH1a8kCS6YwD7fCPxT4MEkn+9q/xa4DTiY5GbgceAGgKo6muQg8DC9O6luqaqzY+9akqbY2MOiqn6PwdchAK5dZJ29wN6RNSVJWpJPcEuSmgwLSVKTYSFJajIsJElNhoUkqcmwkCQ1GRaSpCbDQpLUZFhIkpoMC0lSk2EhSWoyLCRJTYaFJKnJsJAkNRkWkqQmw0KS1GRYSJKaDAtJUpNhIUlqOm/CIsm2JMeSHE+ye9L9SNI0OS/CIska4EPADwJbgRuTbJ1sV5I0Pc6LsACuBo5X1Z9U1V8BB4DtE+5JkqbGBZNuYEjrgRN93+eBv3/uoCS7gF3d168lOTaG3qbBpcCXJ93EapCf2znpFvR8/v181q1Zia38zUHF8yUsBv0vUM8rVO0D9o2+nemSZK6qZifdhzSIfz/H43w5DTUPbOz7vgF4YkK9SNLUOV/C4n8BW5JsTvIyYAdwaMI9SdLUOC9OQ1XVmST/HPhtYA1wR1UdnXBb08RTe1rN/Ps5Bql63ql/SZKe43w5DSVJmiDDQpLUZFhoSb5mRatVkjuSnEry0KR7mQaGhRbla1a0yt0FbJt0E9PCsNBSfM2KVq2q+hTw1KT7mBaGhZYy6DUr6yfUi6QJMiy0lKFesyLpxc+w0FJ8zYokwLDQ0nzNiiTAsNASquoM8OxrVh4BDvqaFa0WSe4B7gNem2Q+yc2T7unFzNd9SJKaPLKQJDUZFpKkJsNCktRkWEiSmgwLSVKTYSFJajIspCEkuSjJj3fzb0rym5PuSRonw0IazkXAj7+QFbpXvEsvCj6UJw0hybOvZz8GfAN4BvgycCXwAHBTVVWSLwJ3AD8A/CK9V2j/B2At8AXgHVX1tSRXAe8DXtVt5+1VdXKRff894KPdPn8P+MGqunJEf1RpII8spOHsBr5QVX8X+EngdcB76P0o1LcDb+wb+5dV9Q+A3wV+Bvj+qno9MAf8qyQvBT4IvLWqrqIXLnuX2PedwI9V1RuAsyv5h5KGdcGkG5DOU/dX1TxAks8Dm+j9v36AX+mm19ALk99PAvAyuncZ0TsiOdzV1wCLHVVcBLy6qv6gK/0y8OYV/ZNIQzAspOU53Td/luf+W3qmmwY4XFU39q+Y5LuBo92RQsug3xSRxs7TUNJwngZe/QLX+TTwxiTfCZDklUm+i951j5kkb+jqL01yxaANVNWfA08nuaYr7VhW99I3ySMLaQhV9ZUkv5/kIeDrwJNDrLOQ5O3APUnWduWfqao/TvJW4ANJ/ga9f4e/ACz2+vebgf+S5Bngk8BffFN/GGkZvBtKWuWSvKqqvtbN7wbWVdW7J9yWpoxHFtLq90NJ9tD79/qnwNsn246mkUcW0iqR5EM89xZcgPdX1Z2T6EfqZ1hIkpq8G0qS1GRYSJKaDAtJUpNhIUlq+v+m1OYgTYRg3wAAAABJRU5ErkJggg==\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "Text(0.5, 1.0, '4G')"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.countplot(df['four_g'])\n",
    "plt.show()\n",
    "sns.countplot(df['three_g'])\n",
    "plt.show()\n",
    "plt.pie(x=df['three_g'].value_counts(),labels=(['Supported','Non-Supported']),autopct='%.1f');\n",
    "plt.title('3G')\n",
    "plt.show()\n",
    "plt.pie(x=df['four_g'].value_counts(),labels=(['Supported','Non-Supported']),autopct='%.1f');\n",
    "plt.title('4G')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 1152x720 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.subplots(figsize=(16,10))\n",
    "sns.countplot(df['int_memory']);\n",
    "plt.xticks(rotation=90);\n",
    "plt.show()\n",
    "sns.distplot(df['int_memory']);"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.distplot(df['px_height'],color='m');"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAYUAAAEGCAYAAACKB4k+AAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjMuMiwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8vihELAAAACXBIWXMAAAsTAAALEwEAmpwYAAASAklEQVR4nO3df7DldV3H8edLllRQE4crrbvYoq0mVoLdKKWMpBR/guYPmBGZstZpwJGyGrGZpJptnFGxJn9MKCgoQgSiaI6CaJJWLrsbyo+VcQvClZVdswKbIqF3f5zvfjzunl0Ocr/3e+7e52Pmzj3fz/l+z3kt7N7X/f76nFQVkiQBPGToAJKk2WEpSJIaS0GS1FgKkqTGUpAkNSuGDvBgHHroobVmzZqhY0jSkrJp06ZvVdXcpOeWdCmsWbOGjRs3Dh1DkpaUJP+6t+c8fCRJaiwFSVJjKUiSGktBktRYCpKkxlKQJDWWgiSpsRQkSY2lIElqlvQdzRLA55/1i0NHAOAXr/380BGkB809BUlSYylIkhpLQZLUWAqSpMZSkCQ1loIkqbEUJEmNpSBJaiwFSVJjKUiSGqe5kLQkbVn/2aEj8JQ/ePbQERacewqSpMY9BUnqydlnnz10BOCB5XBPQZLU9FYKSQ5P8rkkW5LclOT13fjZSb6R5Pru6/lj25yVZGuSW5I8t69skqTJ+jx8dC/whqranOSRwKYkV3fPvaOq3ja+cpIjgZOBpwKPAz6T5ElVdV+PGSVJY3rbU6iq7VW1uXt8N7AFWLWPTU4ELqmqe6rqVmArcExf+SRJe1qUcwpJ1gBHA1/qhs5I8pUk5yc5pBtbBXx9bLNtTCiRJOuSbEyycefOnX3GlqRlp/dSSPII4HLgzKq6C3gP8ETgKGA78PZdq07YvPYYqDq3quaran5ubq6f0JK0TPV6SWqSAxkVwkVV9RGAqrpz7Pn3Ap/oFrcBh49tvhq4o898Q7n9j39y6AgAPP4Pbxg6gqQZ01spJAlwHrClqs4ZG19ZVdu7xZcAN3aPrwQ+nOQcRiea1wIb+sqn+3fsXxw7dAQAvvi6Lw4dYUG88w0fHzoCZ7z9RUNH0Izrc0/hWOBU4IYk13djbwJOSXIUo0NDtwGvBaiqm5JcCtzM6Mql073ySJIWV2+lUFVfYPJ5gk/uY5v1wPq+MkmS9m2/m+bip3/vwqEjsOmtrx46giT9QJzmQpLUWAqSpMZSkCQ1loIkqbEUJEmNpSBJaiwFSVJjKUiSmv3u5jVJD876V71s6Aj8wYcuGzrCsuWegiSpsRQkSY2lIElqLAVJUmMpSJIaS0GS1FgKkqTGUpAkNZaCJKmxFCRJjaUgSWosBUlSYylIkhpLQZLUWAqSpMZSkCQ1loIkqbEUJElNb6WQ5PAkn0uyJclNSV7fjT8mydVJvtZ9P2Rsm7OSbE1yS5Ln9pVNkjRZn3sK9wJvqKqnAD8HnJ7kSOCNwDVVtRa4plume+5k4KnACcC7kxzQYz5J0m56K4Wq2l5Vm7vHdwNbgFXAicAF3WoXACd1j08ELqmqe6rqVmArcExf+SRJe1qUcwpJ1gBHA18CDquq7TAqDuCx3WqrgK+PbbatG5MkLZLeSyHJI4DLgTOr6q59rTphrCa83rokG5Ns3Llz50LFlCTRcykkOZBRIVxUVR/phu9MsrJ7fiWwoxvfBhw+tvlq4I7dX7Oqzq2q+aqan5ub6y+8JC1DfV59FOA8YEtVnTP21JXAad3j04CPjY2fnOShSY4A1gIb+sonSdrTih5f+1jgVOCGJNd3Y28C3gJcmuQ1wO3AywGq6qYklwI3M7py6fSquq/HfJKk3fRWClX1BSafJwA4fi/brAfW95VJkrRv3tEsSWosBUlSYylIkhpLQZLUWAqSpMZSkCQ1loIkqbEUJEmNpSBJaiwFSVJjKUiSGktBktRYCpKkxlKQJDWWgiSpsRQkSY2lIElqLAVJUmMpSJIaS0GS1FgKkqTGUpAkNZaCJKmxFCRJjaUgSWosBUlSM1UpJLlmmjFJ0tK2Yl9PJnkYcBBwaJJDgHRPPQp4XM/ZJEmLbJ+lALwWOJNRAWzie6VwF/Cu/mJJkoawz8NHVfXnVXUE8LtV9YSqOqL7elpVvXNf2yY5P8mOJDeOjZ2d5BtJru++nj/23FlJtia5JclzH/SfTJL0gN3fngIAVfUXSZ4JrBnfpqou3MdmHwDeCey+zjuq6m3jA0mOBE4Gnspor+QzSZ5UVfdNk0+StDCmKoUkHwSeCFwP7PpBXez5A7+pqmuTrJkyx4nAJVV1D3Brkq3AMcA/TLm9JGkBTFUKwDxwZFXVArznGUleDWwE3lBV/w6sAv5xbJ1t3dgekqwD1gE8/vGPX4A4kqRdpr1P4UbgRxbg/d7DaI/jKGA78PZuPBPWnVhAVXVuVc1X1fzc3NwCRJIk7TLtnsKhwM1JNgD37Bqsqhc/kDerqjt3PU7yXuAT3eI24PCxVVcDdzyQ15YkPXjTlsLZC/FmSVZW1fZu8SWM9kAArgQ+nOQcRiea1wIbFuI9JUnTm/bqo88/0BdOcjFwHKMb37YBbwaOS3IUo0NDtzG6D4KquinJpcDNwL3A6V55JEmLb9qrj+7me8f4fwg4EPivqnrU3rapqlMmDJ+3j/XXA+unySNJ6se0ewqPHF9OchKjS0YlSfuRH2iW1Kr6KPDshY0iSRratIePXjq2+BBG9y0sxD0LkqQZMu3VRy8ae3wvo5PEJy54GknSoKY9p/BrfQeRJA1v2g/ZWZ3kim7W0zuTXJ5kdd/hJEmLa9oTze9ndIPZ4xjNSfTxbkyStB+ZthTmqur9VXVv9/UBwImHJGk/M20pfCvJq5Ic0H29Cvi3PoNJkhbftKXw68ArgG8ymt30ZYAnnyVpPzPtJal/ApzWffYBSR4DvI1RWUiS9hPT7in81K5CAKiqbwNH9xNJkjSUaUvhIUkO2bXQ7SlMu5chSVoipv3B/nbg75Ncxmh6i1fgjKaStN+Z9o7mC5NsZDQJXoCXVtXNvSaTJC26qQ8BdSVgEUjSfuwHmjpbkrR/shQkSY2lIElqLAVJUmMpSJIaS0GS1FgKkqTGUpAkNZaCJKmxFCRJjaUgSWosBUlSYylIkpreSiHJ+Ul2JLlxbOwxSa5O8rXu+/gH95yVZGuSW5I8t69ckqS963NP4QPACbuNvRG4pqrWAtd0yyQ5EjgZeGq3zbuTHNBjNknSBL2VQlVdC3x7t+ETgQu6xxcAJ42NX1JV91TVrcBW4Ji+skmSJlvscwqHVdV2gO77Y7vxVcDXx9bb1o3tIcm6JBuTbNy5c2evYSVpuZmVE82ZMFaTVqyqc6tqvqrm5+bmeo4lScvLYpfCnUlWAnTfd3Tj24DDx9ZbDdyxyNkkadlb7FK4Ejite3wa8LGx8ZOTPDTJEcBaYMMiZ5OkZW9FXy+c5GLgOODQJNuANwNvAS5N8hrgduDlAFV1U5JLgZuBe4HTq+q+vrJJkibrrRSq6pS9PHX8XtZfD6zvK48k6f7NyolmSdIMsBQkSY2lIElqLAVJUmMpSJIaS0GS1FgKkqTGUpAkNZaCJKmxFCRJjaUgSWosBUlSYylIkhpLQZLUWAqSpMZSkCQ1loIkqbEUJEmNpSBJaiwFSVJjKUiSGktBktRYCpKkxlKQJDWWgiSpsRQkSY2lIElqLAVJUmMpSJKaFUO8aZLbgLuB+4B7q2o+yWOAvwLWALcBr6iqfx8inyQtV0PuKfxSVR1VVfPd8huBa6pqLXBNtyxJWkSzdPjoROCC7vEFwEnDRZGk5WmoUijgqiSbkqzrxg6rqu0A3ffHTtowybokG5Ns3Llz5yLFlaTlYZBzCsCxVXVHkscCVyf56rQbVtW5wLkA8/Pz1VdASVqOBtlTqKo7uu87gCuAY4A7k6wE6L7vGCKbJC1ni14KSQ5O8shdj4HnADcCVwKndaudBnxssbNJ0nI3xOGjw4Arkux6/w9X1aeSXAdcmuQ1wO3AywfIJknL2qKXQlX9C/C0CeP/Bhy/2HkkSd8zS5ekSpIGZilIkhpLQZLUWAqSpMZSkCQ1loIkqbEUJEmNpSBJaiwFSVJjKUiSGktBktRYCpKkxlKQJDWWgiSpsRQkSY2lIElqLAVJUmMpSJIaS0GS1FgKkqTGUpAkNZaCJKmxFCRJjaUgSWosBUlSYylIkhpLQZLUWAqSpMZSkCQ1M1cKSU5IckuSrUneOHQeSVpOZqoUkhwAvAt4HnAkcEqSI4dNJUnLx0yVAnAMsLWq/qWq/he4BDhx4EyStGykqobO0CR5GXBCVf1Gt3wq8LNVdcbYOuuAdd3ik4FbFjjGocC3Fvg1+2DOhWXOhbUUci6FjNBPzh+tqrlJT6xY4Dd6sDJh7Ptaq6rOBc7tLUCysarm+3r9hWLOhWXOhbUUci6FjLD4OWft8NE24PCx5dXAHQNlkaRlZ9ZK4TpgbZIjkvwQcDJw5cCZJGnZmKnDR1V1b5IzgE8DBwDnV9VNixyjt0NTC8ycC8ucC2sp5FwKGWGRc87UiWZJ0rBm7fCRJGlAloIkqbEUOknOT7IjyY1DZ9mXJIcn+VySLUluSvL6oTPtLsnDkmxI8uUu4x8NnWlfkhyQ5J+SfGLoLHuT5LYkNyS5PsnGofPsTZJHJ7ksyVe7v6PPGDrT7pI8ufvvuOvrriRnDp1rkiS/3f0bujHJxUke1vt7ek5hJMmzgO8AF1bVTwydZ2+SrARWVtXmJI8ENgEnVdXNA0drkgQ4uKq+k+RA4AvA66vqHweONlGS3wHmgUdV1QuHzjNJktuA+aqa6ZutklwA/F1Vva+7gvCgqvqPgWPtVTe1zjcY3ST7r0PnGZdkFaN/O0dW1X8nuRT4ZFV9oM/3dU+hU1XXAt8eOsf9qartVbW5e3w3sAVYNWyq71cj3+kWD+y+ZvK3jySrgRcA7xs6y1KX5FHAs4DzAKrqf2e5EDrHA/88a4UwZgXw8CQrgINYhPu2LIUlLMka4GjgSwNH2UN3SOZ6YAdwdVXNXMbOnwG/D/zfwDnuTwFXJdnUTfUyi54A7ATe3x2Oe1+Sg4cOdT9OBi4eOsQkVfUN4G3A7cB24D+r6qq+39dSWKKSPAK4HDizqu4aOs/uquq+qjqK0V3pxySZuUNySV4I7KiqTUNnmcKxVfV0RjMIn94d7pw1K4CnA++pqqOB/wJmdvr77vDWi4G/HjrLJEkOYTQh6BHA44CDk7yq7/e1FJag7jj95cBFVfWRofPsS3f44G+BE4ZNMtGxwIu74/WXAM9O8qFhI01WVXd033cAVzCaUXjWbAO2je0VXsaoJGbV84DNVXXn0EH24peBW6tqZ1V9F/gI8My+39RSWGK6k7jnAVuq6pyh80ySZC7Jo7vHD2f0l/urg4aaoKrOqqrVVbWG0WGEz1ZV77+JPVBJDu4uKqA7HPMcYOaukquqbwJfT/Lkbuh4YGYugJjgFGb00FHnduDnkhzU/bs/ntE5xF5ZCp0kFwP/ADw5ybYkrxk6014cC5zK6LfaXZfUPX/oULtZCXwuyVcYzWd1dVXN7OWeS8BhwBeSfBnYAPxNVX1q4Ex78zrgou7//VHAnw4bZ7IkBwG/wui375nU7XFdBmwGbmD087r3KS+8JFWS1LinIElqLAVJUmMpSJIaS0GS1FgKkqTGUpAG0E3EJs0cS0HaTZI13bTP7+2mLb6quwlv0ro/luQz3TThm5M8MSNv7aY7viHJK7t1j+umPf8wcEM3P9Rbk1yX5CtJXtuttzLJtd09KDcm+YVF/ONrmZupz2iWZsha4JSq+s1uyuJfBSZNgXER8JaquqKb6/4hwEsZ3bj1NOBQ4Lok13brHwP8RFXd2k1s959V9TNJHgp8MclV3fafrqr13R7FQT3+OaXvYylIk91aVdd3jzcBa3ZfoZt6YlVVXQFQVf/Tjf88cHFV3QfcmeTzwM8AdwEbqurW7iWeA/xUkpd1yz/MqIyuA87v5rj66FgOqXeWgjTZPWOP7wMmHT7KXrbd2ziMZg4dX+91VfXpPV5gNAvqC4APJnlrVV14P3mlBeE5BekH1E1Zvi3JSQBJHtrNqXMt8MrunMEcow+e2TDhJT4N/Fa3R0CSJ3WT3/0ooym938to8sNZnmlU+xn3FKQH51TgL5P8MfBd4OWMprZ+BvBlRh+O8/tV9c0kP77btu9jdFhqczcL5k7gJOA44PeSfJfRR8S+uv8/hjTihHiSpMbDR5KkxsNH0hSSvIvRZ1mM+/Oqev8QeaS+ePhIktR4+EiS1FgKkqTGUpAkNZaCJKmxFCRJzf8D7Ia1lcGFL9QAAAAASUVORK5CYII=\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "cores = sns.countplot(df['n_cores']);"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.boxplot(df['n_cores']);"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.countplot(df['pc']);"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAX0AAAD4CAYAAAAAczaOAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjMuMiwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8vihELAAAACXBIWXMAAAsTAAALEwEAmpwYAAAR9klEQVR4nO3dUYxc133f8e+vtEATjRhL0EqguXRIGHRhUm3oakuo0IsbBRFrF6VcQAEN1CIKAXRVGnWAFA2ZF9sPLFQgjgs9SAVdG6LaNCrRJBBhS01kNobhghK7kmVRFC2YjWRpTULc2IlDFylh0f8+zCEyoIa7s7vkrqTz/QCDe+d/z5l7BhB/e3XmzpxUFZKkPvytlR6AJGn5GPqS1BFDX5I6YuhLUkcMfUnqyHtWegDzuemmm2rjxo0rPQxJekd59tln/7yqJi6vv+1Df+PGjUxPT6/0MCTpHSXJD0bVnd6RpI4Y+pLUEUNfkjpi6EtSRwx9SerI2KGfZFWS7yT5Wnt+Y5Knkny/bW8Yars/yekkLye5a6h+W5IT7diDSXJ1344kaS4LudL/LHBq6Pk+4GhVbQaOtuck2QLsArYCO4CHkqxqfR4G9gCb22PHkkYvSVqQsUI/ySTwceA/DZV3Aofa/iHg7qH6Y1V1oapeAU4D25OsA9ZW1bEa/J7zo0N9JEnLYNwvZ/0H4N8C1w/VbqmqswBVdTbJza2+Hnh6qN1Mq/2s7V9ef4skexj8HwEf+MAHxhyitDTLNdvoGhZaSfNe6Sf5J8C5qnp2zNcc9S+n5qi/tVh1sKqmqmpqYuIt3yKWromqWtDjl37rawvuY+BrpY1zpX8H8E+TfAx4L7A2yX8B3kiyrl3lrwPOtfYzwIah/pPAmVafHFGXJC2Tea/0q2p/VU1W1UYGH9D+z6r658ARYHdrtht4vO0fAXYlWZ1kE4MPbI+3qaDzSW5vd+3cO9RHkrQMlvKDaw8Ah5PcB7wG3ANQVSeTHAZeAt4E9lbVxdbnfuARYA3wZHtIkpbJgkK/qr4JfLPt/wi48wrtDgAHRtSngVsXOkhJ0tXhN3IlqSOGviR1xNCXpI4Y+pLUEUNfkjpi6EtSRwx9SeqIoS9JHTH0Jakjhr4kdcTQl6SOGPqS1BFDX5I6YuhLUkcMfUnqiKEvSR0x9CWpI/OGfpL3Jjme5LtJTib5Qqt/PskPkzzfHh8b6rM/yekkLye5a6h+W5IT7diDba1cSdIyGWe5xAvAr1TVT5NcB3w7yaW1bb9UVb8z3DjJFgYLqG8F3g98I8mH2jq5DwN7gKeBJ4AduE6uJC2bea/0a+Cn7el17VFzdNkJPFZVF6rqFeA0sD3JOmBtVR2rqgIeBe5e0uglSQsy1px+klVJngfOAU9V1TPt0GeSvJDkq0luaLX1wOtD3WdabX3bv7wuSVomY4V+VV2sqm3AJIOr9lsZTNV8ENgGnAW+2JqPmqevOepvkWRPkukk07Ozs+MMUZI0hgXdvVNVfwl8E9hRVW+0PwY/B74MbG/NZoANQ90mgTOtPjmiPuo8B6tqqqqmJiYmFjJESdIcxrl7ZyLJ+9r+GuBXge+1OfpLPgG82PaPALuSrE6yCdgMHK+qs8D5JLe3u3buBR6/em9FkjSfce7eWQccSrKKwR+Jw1X1tST/Ock2BlM0rwKfBqiqk0kOAy8BbwJ72507APcDjwBrGNy14507krSM5g39qnoB+MiI+qfm6HMAODCiPg3cusAxSpKuEr+RK0kdMfQlqSOGviR1xNCXpI4Y+pLUEUNfkjpi6EtSRwx9SeqIoS9JHTH0Jakjhr4kdcTQl6SOGPqS1BFDX5I6YuhLUkcMfUnqiKEvSR0x9CWpI/Mul5jkvcC3gNWt/X+vqs8luRH4b8BGBmvk/npV/UXrsx+4D7gI/Ouq+uNWv42/WSP3CeCzVVVX9y1J8Mtf+BN+8tc/u+bn2bjv69f09X9xzXV893O/dk3Pob6MszD6BeBXquqnSa4Dvp3kSeCfAUer6oEk+4B9wG8l2QLsArYC7we+keRDbXH0h4E9wNMMQn8HLo6ua+Anf/0zXn3g4ys9jCW71n9U1J95p3dq4Kft6XXtUcBO4FCrHwLubvs7gceq6kJVvQKcBrYnWQesrapj7er+0aE+kqRlMNacfpJVSZ4HzgFPVdUzwC1VdRagbW9uzdcDrw91n2m19W3/8vqo8+1JMp1kenZ2dgFvR5I0l7FCv6ouVtU2YJLBVfutczTPqJeYoz7qfAeraqqqpiYmJsYZoiRpDAu6e6eq/hL4JoO5+DfalA1te641mwE2DHWbBM60+uSIuiRpmcwb+kkmkryv7a8BfhX4HnAE2N2a7QYeb/tHgF1JVifZBGwGjrcpoPNJbk8S4N6hPpKkZTDO3TvrgENJVjH4I3G4qr6W5BhwOMl9wGvAPQBVdTLJYeAl4E1gb7tzB+B+/uaWzSfxzh1JWlbzhn5VvQB8ZET9R8CdV+hzADgwoj4NzPV5gCTpGvIbuZLUEUNfkjpi6EtSRwx9SeqIoS9JHTH0Jakjhr4kdcTQl6SOGPqS1BFDX5I6YuhLUkcMfUnqiKEvSR0x9CWpI4a+JHXE0Jekjhj6ktSRcdbI3ZDkT5OcSnIyyWdb/fNJfpjk+fb42FCf/UlOJ3k5yV1D9duSnGjHHmxr5UqSlsk4a+S+CfxmVT2X5Hrg2SRPtWNfqqrfGW6cZAuwC9gKvB/4RpIPtXVyHwb2AE8DTwA7cJ1cSVo2817pV9XZqnqu7Z8HTgHr5+iyE3isqi5U1SvAaWB7knXA2qo6VlUFPArcvdQ3IEka34Lm9JNsZLBI+jOt9JkkLyT5apIbWm098PpQt5lWW9/2L6+POs+eJNNJpmdnZxcyREnSHMYO/SS/APwB8BtV9VcMpmo+CGwDzgJfvNR0RPeao/7WYtXBqpqqqqmJiYlxhyhJmsdYoZ/kOgaB/3tV9YcAVfVGVV2sqp8DXwa2t+YzwIah7pPAmVafHFGXJC2Tce7eCfAV4FRV/e5Qfd1Qs08AL7b9I8CuJKuTbAI2A8er6ixwPsnt7TXvBR6/Su9DkjSGce7euQP4FHAiyfOt9tvAJ5NsYzBF8yrwaYCqOpnkMPASgzt/9rY7dwDuBx4B1jC4a8c7dyRpGc0b+lX1bUbPxz8xR58DwIER9Wng1oUMUJJ09fiNXEnqiKEvSR0x9CWpI4a+JHXE0Jekjhj6ktQRQ1+SOmLoS1JHDH1J6oihL0kdMfQlqSOGviR1xNCXpI6M89PK0jvO9R/ex989tG+lh7Fk138Y4OMrPQy9ixj6elc6f+oBXn3gnR+WG/d9faWHoHcZp3ckqSOGviR1xNCXpI6MszD6hiR/muRUkpNJPtvqNyZ5Ksn32/aGoT77k5xO8nKSu4bqtyU50Y492BZIlyQtk3Gu9N8EfrOqPgzcDuxNsgXYBxytqs3A0facdmwXsBXYATyUZFV7rYeBPcDm9thxFd+LJGke84Z+VZ2tqufa/nngFLAe2Akcas0OAXe3/Z3AY1V1oapeAU4D25OsA9ZW1bGqKuDRoT6SpGWwoDn9JBuBjwDPALdU1VkY/GEAbm7N1gOvD3WbabX1bf/y+qjz7EkynWR6dnZ2IUOUJM1h7NBP8gvAHwC/UVV/NVfTEbWao/7WYtXBqpqqqqmJiYlxhyhJmsdYoZ/kOgaB/3tV9Yet/EabsqFtz7X6DLBhqPskcKbVJ0fUJUnLZJy7dwJ8BThVVb87dOgIsLvt7wYeH6rvSrI6ySYGH9geb1NA55Pc3l7z3qE+kqRlMM7PMNwBfAo4keT5Vvtt4AHgcJL7gNeAewCq6mSSw8BLDO782VtVF1u/+4FHgDXAk+0hSVom84Z+VX2b0fPxAHdeoc8B4MCI+jRw60IGKEm6evxGriR1xNCXpI4Y+pLUEUNfkjpi6EtSRwx9SeqIoS9JHTH0Jakjhr4kdcTQl6SOGPqS1BFDX5I6YuhLUkcMfUnqiKEvSR0x9CWpI4a+JHVknDVyv5rkXJIXh2qfT/LDJM+3x8eGju1PcjrJy0nuGqrfluREO/ZgWydXkrSMxrnSfwTYMaL+para1h5PACTZAuwCtrY+DyVZ1do/DOxhsFD65iu8piTpGpo39KvqW8CPx3y9ncBjVXWhql4BTgPbk6wD1lbVsaoq4FHg7kWOWZK0SEuZ0/9Mkhfa9M8NrbYeeH2ozUyrrW/7l9dHSrInyXSS6dnZ2SUMUZI0bLGh/zDwQWAbcBb4YquPmqevOeojVdXBqpqqqqmJiYlFDlGSdLlFhX5VvVFVF6vq58CXge3t0AywYajpJHCm1SdH1CVJy2hRod/m6C/5BHDpzp4jwK4kq5NsYvCB7fGqOgucT3J7u2vnXuDxJYxbkrQI75mvQZLfBz4K3JRkBvgc8NEk2xhM0bwKfBqgqk4mOQy8BLwJ7K2qi+2l7mdwJ9Aa4Mn2kCQto3lDv6o+OaL8lTnaHwAOjKhPA7cuaHSSpKvKb+RKUkcMfUnqiKEvSR0x9CWpI4a+JHXE0Jekjhj6ktQRQ1+SOmLoS1JHDH1J6si8P8MgvVNt3Pf1lR7Ckv3imutWegh6lzH09a706gMfv+bn2Ljv68tyHulqcnpHkjpi6EtSRwx9SeqIoS9JHTH0Jakj84Z+kq8mOZfkxaHajUmeSvL9tr1h6Nj+JKeTvJzkrqH6bUlOtGMPtrVyJUnLaJwr/UeAHZfV9gFHq2ozcLQ9J8kWYBewtfV5KMmq1udhYA+DxdI3j3hNSdI1Nm/oV9W3gB9fVt4JHGr7h4C7h+qPVdWFqnoFOA1sT7IOWFtVx6qqgEeH+kiSlsli5/RvqaqzAG17c6uvB14fajfTauvb/uV1SdIyutof5I6ap6856qNfJNmTZDrJ9Ozs7FUbnCT1brGh/0absqFtz7X6DLBhqN0kcKbVJ0fUR6qqg1U1VVVTExMTixyiJOlyiw39I8Dutr8beHyovivJ6iSbGHxge7xNAZ1Pcnu7a+feoT6SpGUy7w+uJfl94KPATUlmgM8BDwCHk9wHvAbcA1BVJ5McBl4C3gT2VtXF9lL3M7gTaA3wZHtIkpbRvKFfVZ+8wqE7r9D+AHBgRH0auHVBo5MkXVV+I1eSOmLoS1JHDH1J6oihL0kdMfQlqSOGviR1xNCXpI4Y+pLUEUNfkjpi6EtSRwx9SeqIoS9JHTH0Jakjhr4kdcTQl6SOGPqS1BFDX5I6YuhLUkeWFPpJXk1yIsnzSaZb7cYkTyX5ftveMNR+f5LTSV5OctdSBy9JWpircaX/j6pqW1VNtef7gKNVtRk42p6TZAuwC9gK7AAeSrLqKpxfkjSmazG9sxM41PYPAXcP1R+rqgtV9QpwGth+Dc4vSbqCpYZ+AX+S5Nkke1rtlqo6C9C2N7f6euD1ob4zrfYWSfYkmU4yPTs7u8QhSpIuec8S+99RVWeS3Aw8leR7c7TNiFqNalhVB4GDAFNTUyPbSJIWbklX+lV1pm3PAX/EYLrmjSTrANr2XGs+A2wY6j4JnFnK+SVJC7Po0E/yt5Ncf2kf+DXgReAIsLs12w083vaPALuSrE6yCdgMHF/s+SVJC7eU6Z1bgD9Kcul1/mtV/Y8k/xs4nOQ+4DXgHoCqOpnkMPAS8Cawt6ouLmn0kqQFWXToV9WfAb88ov4j4M4r9DkAHFjsOSVJS+M3ciWpI4a+JHXE0Jekjhj6ktQRQ1+SOmLoS1JHDH1J6shSf3tHetdoXzRcWJ9/v/DzVPlzUlo5hr7UGMbqgdM7ktQRQ1+SOmLoS1JHDH1J6oihL0kdMfQlqSOGviR1xNCXpI7k7f6FlCSzwA9WehzSCDcBf77Sg5Cu4JeqauLy4ts+9KW3qyTTVTW10uOQFsLpHUnqiKEvSR0x9KXFO7jSA5AWyjl9SeqIV/qS1BFDX5I6YuhLUkcMfWkeGfDfit4V/A9ZGiHJxiSnkjwEPAd8Jcl0kpNJvjDU7tUk/y7JsXb87yf54yT/J8m/XLl3II3mGrnSlf0d4F9U1b9KcmNV/TjJKuBokr9XVS+0dq9X1T9M8iXgEeAO4L3ASeA/rsjIpSvwSl+6sh9U1dNt/9eTPAd8B9gKbBlqd6RtTwDPVNX5qpoF/l+S9y3baKUxeKUvXdn/BUiyCfg3wD+oqr9I8giDK/lLLrTtz4f2Lz3335jeVrzSl+a3lsEfgJ8kuQX4xys8HmnRvAqR5lFV303yHQZz9H8G/K8VHpK0aP4MgyR1xOkdSeqIoS9JHTH0Jakjhr4kdcTQl6SOGPqS1BFDX5I68v8BbKpnYMgAmzkAAAAASUVORK5CYII=\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.distplot(df['ram']);\n",
    "plt.show()\n",
    "df['ram'].plot.box();"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.countplot(df['wifi'])\n",
    "plt.pie(x=df['wifi'].value_counts(),labels=['Yes','No'],radius=2,explode=(0,0.03),colors=['m','c'],autopct='%.2f');\n",
    "plt.pie([1],colors='w',radius=1);"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 576x504 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.pointplot(y='ram',x='price_range',data=df);\n",
    "plt.show()\n",
    "plt.subplots(figsize=(8,7))\n",
    "sns.boxplot(df['price_range'],df['ram']);"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "df.groupby('price_range')['battery_power'].mean().plot(kind='bar');\n",
    "plt.show()\n",
    "sns.pointplot(y='battery_power',x='price_range',data=df);"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='price_range', ylabel='battery_power'>"
      ]
     },
     "execution_count": 56,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.barplot(df['price_range'],df['battery_power'])\n",
    "#Battery power does increase the price of phones\n",
    "plt.show()\n",
    "sns.boxplot(df['price_range'],df['battery_power'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "metadata": {},
   "outputs": [],
   "source": [
    "blue = pd.crosstab(df['blue'],df['price_range'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th>price_range</th>\n",
       "      <th>0</th>\n",
       "      <th>1</th>\n",
       "      <th>2</th>\n",
       "      <th>3</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>blue</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>257</td>\n",
       "      <td>255</td>\n",
       "      <td>257</td>\n",
       "      <td>241</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>243</td>\n",
       "      <td>245</td>\n",
       "      <td>243</td>\n",
       "      <td>259</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "price_range    0    1    2    3\n",
       "blue                           \n",
       "0            257  255  257  241\n",
       "1            243  245  243  259"
      ]
     },
     "execution_count": 71,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "blue"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='blue'>"
      ]
     },
     "execution_count": 72,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "blue.div(blue.sum(1).astype(float),axis=0).plot(kind='bar')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='price_range', ylabel='blue'>"
      ]
     },
     "execution_count": 73,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.barplot(df['price_range'],df['blue'])\n",
    "#We can infer that the price is not affected by bluetooth, since bluetooth is there in almost every range of phone"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.barplot(df['price_range'],df['clock_speed'])\n",
    "plt.show()\n",
    "df.groupby('price_range')['clock_speed'].mean().plot(kind='bar')\n",
    "plt.show()\n",
    "#clock speed is almost same for all the mobile phones"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='price_range', ylabel='dual_sim'>"
      ]
     },
     "execution_count": 75,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.barplot(df['price_range'],df['dual_sim'])\n",
    "#Dual sim is present in all the phones and it doesn't affect the price"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAXgAAAEHCAYAAACk6V2yAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjMuMiwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8vihELAAAACXBIWXMAAAsTAAALEwEAmpwYAAANwUlEQVR4nO3df6zddX3H8deLtgzBRqK9EwboBcNwxB+wXupIDSphDf7I5jLNaCIugdnF+QOyTbJliUaXZQkkbM4tm40SfyKo6LKQDCQZSGAUuLfjd3ExDKVI00tYgTIU2r72x/1Wzi237Wl7P/d7z7vPR3Jzzzn33PN55wSe/d7v+Z7vcRIBAOo5ou8BAABtEHgAKIrAA0BRBB4AiiLwAFDU0r4HGLRixYqMj4/3PQYAjIypqaknk4zN9bNFFfjx8XFNTk72PQYAjAzbP9nbz5oG3vajkp6VtFPSjiQTLdcDALxkIbbg35XkyQVYBwAwgBdZAaCo1oGPpB/YnrK9bq472F5ne9L25PT0dONxAODw0Trwq5P8pqR3S/qY7XP2vEOS9UkmkkyMjc35QjAA4CA0DXySn3Xft0r6vqRVLdcDALykWeBtH2N7+e7LktZIeqDVegCA2VoeRfNaSd+3vXudq5Pc0HA9AMCAZoFP8oikt7Z6fACzXXbZZdqyZYuOO+44XX755X2Pg0VgUb2TFcDB27Jlix5//PG+x8AiwnHwAFAUgQeAothFg96wzxhoi8CjN+wzBtoi8AAwhwp/YRJ4AJhDhb8weZEVAIoi8ABQFIEHgKIIPAAUReABoCgCDwBFEXgAKIrAA0BRvNEJmAerv7C67xF05LYjdYSO0GPbHut1nts/cXtva2M2tuABoCi24A9AhXNTADh8EPgDUOHcFAAOH+yiAYCiCDwAFEXgAaAo9sEfxn76uTf3uv6Op14taal2PPWT3md53afv73V9oAUCD2DR+eE57+h7BD2/dIlk6/nNm3ud5x23/vCgf5ddNABQFIEHgKIIPAAUReABoCgCDwBFEXgAKIrAA0BRBB4AiuKNTkAROTrapV3K0el7FCwSzQNve4mkSUmPJ3nfoTzWyk99bX6GOkjLn3xWSyT99Mlne59l6ooP97o+Fp8XV7/Y9whYZBZiF80lkjYtwDoAgAFNA2/7REnvlfSllusAAF6u9Rb830u6TNKuxusAAPbQLPC23ydpa5Kp/dxvne1J25PT09OtxgGAw07LLfjVkn7H9qOSrpF0ru1v7HmnJOuTTCSZGBsbazgOABxemgU+yV8mOTHJuKQLJP1Hkg+1Wg8AMBvHwaM3K47aJWlH9x3AfFuQwCe5RdItC7EWRsefv2Vb3yMAe3VsMuv7KGILHgDm8KGdo/+XJeeiAYCiCDwAFEXgAaAoAg8ARRF4ACiKwANAUQQeAIriOPgDsOvIY2Z9B4DFjMAfgOdOXdP3CAAwNHbRAEBRBB4AiiLwAFAUgQeAogg8ABRF4AGgKAIPAEUReAAoisADQFEEHgCKIvAAUBSBB4CiCDwAFEXgAaAoAg8ARRF4ACiKwANAUQQeAIoi8ABQFIEHgKIIPAAUReABoCgCDwBFEXgAKKpZ4G0fZfsu2/faftD2Z1utBQB4uaUNH/sXks5Nst32Mkm32f73JBsargkA6DQLfJJI2t5dXdZ9pdV6AIDZmu6Dt73E9j2Stkq6Kcmdc9xnne1J25PT09MtxwGAw0rTwCfZmeQMSSdKWmX7TXPcZ32SiSQTY2NjLccBgMPKghxFk2SbpFsknb8Q6wEA2h5FM2b72O7yKySdJ+nhVusBAGZreRTN8ZK+anuJZv4h+XaS6xuuBwAY0PIomvskndnq8QEA+8Y7WQGgKAIPAEUReAAoisADQFEEHgCKIvAAUBSBB4CiCDwAFEXgAaAoAg8ARRF4AChqv4G3/Xu2XzVw/Vjb7286FQDgkA2zBf+ZJE/vvtKd2/0zzSYCAMyLYQI/131anmYYADAPhgn8pO0rbb/B9im2/07SVOvBAACHZq+Bt/317uIjkl6QdK2k70j6uaSPtR8NAHAo9rWrZaXt10v6oKR3SbpCUrqf/Yqk5xrPBgA4BPsK/L9IukHSKZImB263ZkJ/SsO5AACHaK+7aJL8Q5LfkHRVklMGvk5OQtwBYJHb74usST66EIMAAOYX72QFgKIIPAAUReABoCgCDwBFEXgAKIrAA0BRBB4AiiLwAFAUgQeAogg8ABRF4AGgKAIPAEUReAAoisADQFHNAm/7JNs3295k+0Hbl7RaCwDwcvv6RKdDtUPSnyXZaHu5pCnbNyV5qOGaAIBOsy34JE8k2dhdflbSJkkntFoPADDbguyDtz0u6UxJd87xs3W2J21PTk9PL8Q4AHBYaB5426+UdJ2kS5M8s+fPk6xPMpFkYmxsrPU4AHDYaBp428s0E/dvJvley7UAALO1PIrGkr4saVOSK1utAwCYW8st+NWSLpR0ru17uq/3NFwPADCg2WGSSW6T5FaPDwDYN97JCgBFEXgAKIrAA0BRBB4AiiLwAFAUgQeAogg8ABRF4AGgKAIPAEUReAAoisADQFEEHgCKIvAAUBSBB4CiCDwAFEXgAaAoAg8ARRF4ACiKwANAUQQeAIoi8ABQFIEHgKIIPAAUReABoCgCDwBFEXgAKIrAA0BRBB4AiiLwAFAUgQeAogg8ABRF4AGgKAIPAEU1C7ztq2xvtf1AqzUAAHvXcgv+K5LOb/j4AIB9aBb4JLdKeqrV4wMA9q33ffC219metD05PT3d9zgAUEbvgU+yPslEkomxsbG+xwGAMnoPPACgDQIPAEW1PEzyW5LukHSa7c22L261FgDg5Za2euAka1s9NgBg/9hFAwBFEXgAKIrAA0BRBB4AiiLwAFAUgQeAogg8ABRF4AGgKAIPAEUReAAoisADQFEEHgCKIvAAUBSBB4CiCDwAFEXgAaAoAg8ARRF4ACiKwANAUQQeAIoi8ABQFIEHgKIIPAAUReABoCgCDwBFEXgAKIrAA0BRBB4AiiLwAFAUgQeAogg8ABRF4AGgKAIPAEUReAAoqmngbZ9v+0e2f2z7L1quBQCYrVngbS+R9E+S3i3pdElrbZ/eaj0AwGwtt+BXSfpxkkeSvCDpGkm/23A9AMAAJ2nzwPYHJJ2f5I+66xdKeluSj+9xv3WS1nVXT5P0oyYDzZ8Vkp7se4hCeD7nF8/n/BqF5/P1Scbm+sHShot6jtte9q9JkvWS1jecY17Znkwy0fccVfB8zi+ez/k16s9ny100myWdNHD9REk/a7geAGBAy8DfLelU2yfbPlLSBZL+reF6AIABzXbRJNlh++OSbpS0RNJVSR5std4CGpndSSOC53N+8XzOr5F+Ppu9yAoA6BfvZAWAogg8ABRF4A8Ap16YP7avsr3V9gN9zzLqbJ9k+2bbm2w/aPuSvmcaZbaPsn2X7Xu75/Ozfc90sNgHP6Tu1Av/Lem3NXMI6N2S1iZ5qNfBRpTtcyRtl/S1JG/qe55RZvt4Sccn2Wh7uaQpSe/nv82DY9uSjkmy3fYySbdJuiTJhp5HO2BswQ+PUy/MoyS3Snqq7zkqSPJEko3d5WclbZJ0Qr9Tja7M2N5dXdZ9jeSWMIEf3gmSHhu4vln8T4RFxva4pDMl3dnzKCPN9hLb90jaKummJCP5fBL44Q116gWgL7ZfKek6SZcmeabveUZZkp1JztDMO/BX2R7J3YgEfnicegGLVrev+DpJ30zyvb7nqSLJNkm3SDq/30kODoEfHqdewKLUvSj4ZUmbklzZ9zyjzvaY7WO7y6+QdJ6kh3sd6iAR+CEl2SFp96kXNkn6dpFTL/TC9rck3SHpNNubbV/c90wjbLWkCyWda/ue7us9fQ81wo6XdLPt+zSzYXdTkut7numgcJgkABTFFjwAFEXgAaAoAg8ARRF4ACiKwANAUQQeAIoi8CjL9udsn9f3HEBfOA4eJdlekmTnqD02MJ/YgsfIsT1u+2HbX7V9n+3v2j7a9qO2P237NkkftP0V2x/ofucs2//ZfYjDXbaXd2cMvML23d3j/PE+1nxn96EaV0u6v7vtX21PdR8KsW7gvttt/0231gbbr+1uf0N3/e7ur4vtA7/zqYE5RvYDJrC4EHiMqtMkrU/yFknPSPqT7vafJ3l7kmt237E7d9C1mvnQhrdq5twiz0u6WNLTSc6SdJakj9g+eR9rrpL0V0lO765flGSlpAlJn7T9mu72YyRt6Na6VdJHuts/L+nz3Xq/PFGd7TWSTu0e/wxJK7sPRAEOCYHHqHosye3d5W9Ient3+do57nuapCeS3C1JSZ7pzi20RtKHu/N+3ynpNZoJ7d7cleR/Bq5/0va9kjZo5kyju3/3BUm7z10yJWm8u3y2pO90l68eeJw13dd/Sdoo6Y37mQMYytK+BwAO0p4vHu2+/twc9/Uc9999+yeS3Djkmr98bNvv1MxfAmcn+T/bt0g6qvvxi3npxa2d2v//Z5b0t0m+OOQcwFDYgseoep3ts7vLazXzuZl787CkX7N9liR1+9+XaubMoB/tzqUu279u+5gh13+VpP/t4v5GSb81xO9skPT73eULBm6/UdJF3Qd2yPYJtn91yDmAvSLwGFWbJP1hd0rXV0v6573dsfsM3T+Q9IVul8pNmtna/pKkhyRttP2ApC9q+L9qb5C0tFv/rzUT7/25VNKf2r5LM6ekfbqb7wea2WVzh+37JX1X0vIh5wD2isMkMXK6zx29PslIfYya7aMlPZ8kti+QtDYJH9yOZtgHDyyclZL+sfsEpm2SLup3HFTHFjwwwPabJX19j5t/keRtfcwDHAoCDwBF8SIrABRF4AGgKAIPAEUReAAo6v8B9sdfIYUGfagAAAAASUVORK5CYII=\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.barplot(df['price_range'],df['fc'])\n",
    "plt.show()\n",
    "#FC is better for expensive phones"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.barplot(df['price_range'],df['four_g']);"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "#sns.barplot(df['price_range'],df['int_memory'])\n",
    "#plt.show\n",
    "sns.boxplot(df['price_range'],df['int_memory'])\n",
    "plt.show()\n",
    "sns.pointplot(df['price_range'],df['int_memory']);"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 83,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='price_range', ylabel='mobile_wt'>"
      ]
     },
     "execution_count": 83,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAYYAAAEHCAYAAACqbOGYAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjMuMiwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8vihELAAAACXBIWXMAAAsTAAALEwEAmpwYAAAUCElEQVR4nO3dfbRddX3n8ffHRESQjmIumPIU6kqxgPh0pTo4yiqimdYaViud0KVNB9rMg1UcqwjjjEw7izWOdjrjOGOXGaSmLQVTcQbqrFGzMiLFGkICyFOkMFIgEMhVioBaNPCdP84Onh1uyD0359x9H96vtc7ae//203edleST/dv7/HaqCkmSdntO1wVIkmYXg0GS1GIwSJJaDAZJUovBIElqWdx1AftryZIltWzZsq7LkKQ5ZevWrd+pqrHJ1s35YFi2bBlbtmzpugxJmlOS3LO3dXYlSZJaDAZJUovBIElqMRgkSS0GgySpxWCQJLUYDJKkFoNBktQy53/gJmn6zjvvPB588EFe8pKX8LGPfazrcjRLGAzSAvbggw9y//33d12GZhm7kiRJLQaDJKnFrqQZYD/ucPl9SqNlMMwA+3GHaz59n6d88pROz3/AIwfwHJ7DfY/c13ktX3/P1zs9v37CriRJUstIgyHJJUl2Jrl1knUfSFJJlvS1XZDkriR3JHnrKGuTJE1u1FcMnwVW7NmY5CjgdODevrbjgVXACc0+n0qyaMT1SZL2MNJ7DFV1TZJlk6z6z8B5wJV9bSuBy6vqCeDuJHcBJwPf2N86XvPBP9nfQ+yXQ77zGIuAe7/zWOe1bP34b+zX/vf+/suHVMn07Xr4UGAxux6+p9N6jv7ILZ2dWxqlGb/5nOTtwP1V9c0k/auOADb1LW9v2iY7xhpgDcDRRx89okql+a8OKp7iKeqg6rqUeWG+PDE3o8GQ5CDgw8BbJls9Sdukf1qrai2wFmB8fNw/0dI0/fiUH3ddwrwyX56Ym+krhpcCxwK7rxaOBG5IcjK9K4Sj+rY9EnhghuuTpAVvRh9XrapbquqwqlpWVcvohcGrq+pB4CpgVZLnJTkWWA5snsn6JEmjf1z1Mno3j49Lsj3JOXvbtqpuA9YDtwNfAt5dVU+Osj5J0jON+qmks/axftkeyxcBF42ypi48dcDBran2z5IDnwJ2NVPpJ772xjd1ev4fLl4ECT/cvr3zWt50zdemva9DYsyA7y+f7F67pusDJz3SdQnSvOaQGJKkFoNBktRiMEiSWrzHIElD8sKq1nSuMhgkaUje+eT8eFLOriRJUovBIElqMRgkSS0GgySpxWCQJLUYDJKkFoNBktRiMEiSWgwGSVKLwSBJajEYJEktBoMkqcVgkCS1jDQYklySZGeSW/vaPp7kW0luTvI/k7ywb90FSe5KckeSt46yNknS5EZ9xfBZYMUebRuAE6vqJOBvgAsAkhwPrAJOaPb5VJJFI65PkrSHkQZDVV0DPLxH21eqalezuAk4splfCVxeVU9U1d3AXcDJo6xPkvRMXd9jOBv4P838EcB9feu2N23PkGRNki1JtkxMTIy4RElaWDoLhiQfBnYBl+5ummSzSd+PV1Vrq2q8qsbHxsZGVaIkLUidvNozyWrgbcBpVU+/HHU7cFTfZkcCD8x0bZK00M34FUOSFcCHgLdX1Q/6Vl0FrEryvCTHAsuBzTNdnyQtdCO9YkhyGXAqsCTJduBCek8hPQ/YkARgU1X986q6Lcl64HZ6XUzvrqonR1mfJOmZRhoMVXXWJM2feZbtLwIuGl1FkqR96fqpJEnSLGMwSJJaDAZJUovBIElqMRgkSS0GgySpxWCQJLUYDJKkFoNBktRiMEiSWgwGSVKLwSBJajEYJEktBoMkqcVgkCS1GAySpBaDQZLUYjBIkloMBklSy0iDIcklSXYmubWv7dAkG5Lc2Uxf1LfugiR3JbkjyVtHWZskaXKjvmL4LLBij7bzgY1VtRzY2CyT5HhgFXBCs8+nkiwacX2SpD2MNBiq6hrg4T2aVwLrmvl1wBl97ZdX1RNVdTdwF3DyKOuTJD1TF/cYDq+qHQDN9LCm/Qjgvr7ttjdtkqQZNJtuPmeStpp0w2RNki1JtkxMTIy4LElaWLoIhoeSLAVopjub9u3AUX3bHQk8MNkBqmptVY1X1fjY2NhIi5WkhaaLYLgKWN3Mrwau7GtfleR5SY4FlgObO6hPkha0xaM8eJLLgFOBJUm2AxcCHwXWJzkHuBc4E6CqbkuyHrgd2AW8u6qeHGV9kqRnGmkwVNVZe1l12l62vwi4aHQVSZL2ZTbdfJYkzQIGgySpxWCQJLUYDJKklikHQ5Jzp9ImSZrbBrliWD1J228OqQ5J0iyxz8dVk5wF/DpwbJKr+lYdAnx3VIVJkroxld8x/DWwA1gC/Ke+9seAm0dRlCSpO/sMhqq6B7gnycXAA1V15+jLkiR1ZZBfPh8DfDrJMcBW4K+Av6qqm0ZRmCSpG1O++VxVH6mqXwBOBK4FPkgvICRJ88iUrxiS/BvgFOAFwI3AB+hdNUiS5pFBupJ+hd6op/8b+Bqwqar+fiRVSZI6M0hX0qvpjYq6GTgduCXJtaMqTJLUjUG6kk4E/hHwJmCc3vuZ7UqSpHlmkK6k/0ivC+m/AtdX1Y9HU5IkqUtTDoaq+qVnW5/kiqr61f0vSZLUpWGOrvozQzyWJKkjwwyGGuKxJEkd8X0MkqSWYQZDBto4+VdJbktya5LLkhyY5NAkG5Lc2UxfNMT6JElTMFAwJHl+kuP2svpDAxznCOC9wHhVnQgsAlYB5wMbq2o5sLFZliTNoEHe4PbLwE3Al5rlV/a/n6GqvjLguRcDz0+yGDgIeABYCaxr1q8DzhjwmJKk/TTIFcO/A04GHgFoRlVdNp2TVtX9wB8A99J718P3mmA5vKp2NNvsAA6bbP8ka5JsSbJlYmJiOiVIkvZikGDYVVXfG8ZJm3sHK4FjgZ8GDk7yzqnuX1Vrq2q8qsbHxsaGUZIkqTFIMNya5NeBRUmWJ/kkvbe7TcebgburaqL5BfUXgH8IPJRkKUAz3TnN40uSpmmQYHgPcALwBHAZ8Cjwvmme917gdUkOShJ6g/NtA64CVjfbrAaunObxJUnTNMiQGD8APtx89ktVXZfk88AN9IbyvhFYS+9dD+uTnEMvPM7c33NJkgazz2BI8pc8y6+aq+rt0zlxVV0IXLhH8xP0rh4kSR2ZyhXDH4y8CknSrLHPYKiqr81EIZKk2WEqXUnrq+rXktxCu0spQFXVSSOrTpI046bSlXRuM33bKAuRJM0O+3xcte+XyPfQuzn8CuAk4ImmTZI0jwwyVtJvAZuBXwHeAWxKcvaoCpMkdWOQdz5/EHhVVX0XIMmL6f3y+ZJRFCZJ6sYgv3zeDjzWt/wYcN9wy5EkdW0qTyW9v5m9H7guyZX0nk5aSa9rSZI0j0ylK+mQZvr/ms9ujmMkSfPQVH7g9nv9y0kO6TXX4yOrSpLUmUGeSjoxyY3ArcBtSbYmOWF0pUmSujDIzee1wPur6piqOgb4XeB/jKYsSVJXBgmGg6vqq7sXqupq4OChVyRJ6tQgv2P4dpJ/C/xps/xO4O7hlyRJ6tIgVwxnA2PAFfRexbkE+M0R1CRJ6tAgwfBS4Khmn+fSe6HONaMoSpLUnUG6ki4FPkDvqaSnRlOOJKlrgwTDRFX95cgqkSTNCoMEw4VJLgY20ht+G4Cq+sJ0TpzkhcDFwIn0htg4G7gD+BywDPhb4Neq6u+mc3xJ0vQMco/hnwKvBFYAv9x89uflPZ8AvlRVL6P3jodtwPnAxqpaTi+Azt+P40uSpmGQK4ZXVNXLh3HSJD8FvJHmqaaq+hHwoyQrgVObzdYBVwMfGsY5JUlTM8gVw6Ykxw/pvD8DTAB/nOTGJBcnORg4vO+NcTuAwybbOcmaJFuSbJmYmBhSSZIkGCwY3gDclOSOJDcnuSXJzdM872Lg1cAfVdWrgO8zQLdRVa2tqvGqGh8bG5tmCZKkyQzSlbRiiOfdDmyvquua5c/TC4aHkiytqh1JlgI7h3hOSdIUTDkYquqeYZ20qh5Mcl+S46rqDno/lru9+awGPtpMfeeDJM2wQa4Yhu09wKVJDgC+Te+pp+cA65OcA9wLnNlhfZK0IHUWDFV1EzA+yarTZrgUSVKfQW4+S5IWAINBktRiMEiSWgwGSVKLwSBJajEYJEktBoMkqcVgkCS1GAySpBaDQZLUYjBIkloMBklSi8EgSWoxGCRJLQaDJKnFYJAktRgMkqQWg0GS1GIwSJJaOg2GJIuS3Jjki83yoUk2JLmzmb6oy/okaSHq+orhXGBb3/L5wMaqWg5sbJYlSTOos2BIciTwS8DFfc0rgXXN/DrgjBkuS5IWvC6vGP4LcB7wVF/b4VW1A6CZHjbZjknWJNmSZMvExMTIC5WkhaSTYEjyNmBnVW2dzv5VtbaqxqtqfGxsbMjVSdLCtrij854CvD3JLwIHAj+V5M+Ah5IsraodSZYCOzuqT5IWrE6uGKrqgqo6sqqWAauA/1tV7wSuAlY3m60GruyiPklayLp+KmlPHwVOT3IncHqzLEmaQV11JT2tqq4Grm7mvwuc1mU9krTQzbYrBklSxwwGSVKLwSBJajEYJEktBoMkqcVgkCS1GAySpBaDQZLUYjBIkloMBklSi8EgSWoxGCRJLQaDJKnFYJAktRgMkqQWg0GS1GIwSJJaDAZJUovBIElq6SQYkhyV5KtJtiW5Lcm5TfuhSTYkubOZvqiL+iRpIevqimEX8LtV9XPA64B3JzkeOB/YWFXLgY3NsiRpBnUSDFW1o6puaOYfA7YBRwArgXXNZuuAM7qoT5IWss7vMSRZBrwKuA44vKp2QC88gMM6LE2SFqROgyHJC4ArgPdV1aMD7LcmyZYkWyYmJkZXoCQtQJ0FQ5Ln0guFS6vqC03zQ0mWNuuXAjsn27eq1lbVeFWNj42NzUzBkrRAdPVUUoDPANuq6g/7Vl0FrG7mVwNXznRtkrTQLe7ovKcA7wJuSXJT0/avgY8C65OcA9wLnNlNeZK0cHUSDFV1LZC9rD5tJmuRJLV1/lSSJGl2MRgkSS0GgySpxWCQJLUYDJKkFoNBktRiMEiSWgwGSVKLwSBJajEYJEktBoMkqcVgkCS1GAySpBaDQZLUYjBIkloMBklSi8EgSWoxGCRJLQaDJKnFYJAktcy6YEiyIskdSe5Kcn7X9UjSQjOrgiHJIuC/A/8YOB44K8nx3VYlSQvLrAoG4GTgrqr6dlX9CLgcWNlxTZK0oKSquq7haUneAayoqt9qlt8F/HxV/c4e260B1jSLxwF3zGih07ME+E7XRcwjfp/D43c5XHPl+zymqsYmW7F4pivZh0zS9ozkqqq1wNrRlzM8SbZU1XjXdcwXfp/D43c5XPPh+5xtXUnbgaP6lo8EHuioFklakGZbMFwPLE9ybJIDgFXAVR3XJEkLyqzqSqqqXUl+B/gysAi4pKpu67isYZlTXV9zgN/n8PhdDtec/z5n1c1nSVL3ZltXkiSpYwaDJKnFYJgBDvMxPEkuSbIzya1d1zLXJTkqyVeTbEtyW5Jzu65pLktyYJLNSb7ZfJ+/13VN0+U9hhFrhvn4G+B0eo/jXg+cVVW3d1rYHJXkjcDjwJ9U1Yld1zOXJVkKLK2qG5IcAmwFzvDP5vQkCXBwVT2e5LnAtcC5VbWp49IG5hXD6DnMxxBV1TXAw13XMR9U1Y6quqGZfwzYBhzRbVVzV/U83iw+t/nMyf95GwyjdwRwX9/ydvzLp1kmyTLgVcB1HZcypyVZlOQmYCewoarm5PdpMIzelIb5kLqS5AXAFcD7qurRruuZy6rqyap6Jb1RG05OMie7Ow2G0XOYD81aTV/4FcClVfWFruuZL6rqEeBqYEW3lUyPwTB6DvOhWam5WfoZYFtV/WHX9cx1ScaSvLCZfz7wZuBbnRY1TQbDiFXVLmD3MB/bgPXzaJiPGZfkMuAbwHFJtic5p+ua5rBTgHcBv5Dkpubzi10XNYctBb6a5GZ6/yHcUFVf7LimafFxVUlSi1cMkqQWg0GS1GIwSJJaDAZJUovBIElqMRgkSS0Gg7SHJL+f5M1d1yF1xd8xSH2SLKqqJ+fasaVh8opBC0aSZUm+lWRdkpuTfD7JQUn+NslHklwLnJnks0ne0ezz2iR/3bx8ZXOSQ5oRND+e5PrmOP/sWc55avMynD8Hbmna/leSrc3LXNb0bft4kouac21KcnjT/tJm+frmaubxvn0+2FfHnH0xjGYXg0ELzXHA2qo6CXgU+JdN+99X1Ruq6vLdGzZjW32O3stWXkFv7JsfAucA36uq1wKvBX47ybHPcs6TgQ9X1fHN8tlV9RpgHHhvkhc37QcDm5pzXQP8dtP+CeATzfmeHoAxyVuA5c3xXwm8pnmRkbRfDAYtNPdV1deb+T8D3tDMf26SbY8DdlTV9QBV9Wgz9tVbgN9oxt2/DngxvX+g92ZzVd3dt/zeJN8ENtEbeXf3vj8Cdo+tsxVY1sy/HviLZv7P+47zluZzI3AD8LJ91CFNyeKuC5Bm2J431XYvf3+SbTPJ9rvb31NVX57iOZ8+dpJT6V15vL6qfpDkauDAZvWP6yc3/Z5k338/A/yHqvr0FOuQpsQrBi00Ryd5fTN/Fr338u7Nt4CfTvJagOb+wmJ6I+X+i+ZdBiT52SQHT/H8/wD4uyYUXga8bgr7bAJ+tZlf1df+ZeDs5kU7JDkiyWFTrEPaK4NBC802YHUzNPKhwB/tbcPmHd3/BPhk0/Wzgd7/7i8GbgduSHIr8GmmfvX9JWBxc/5/T+8f/X15H/D+JJvpDe38vaa+r9DrWvpGkluAzwOHTLEOaa98XFULRvNe4y9W1Zx63WKSg4AfVlUlWQWcVVUru65L85f3GKTZ7zXAf2veuPYIcHa35Wi+84pBGoIkLwf+dI/mJ6rq57uoR9ofBoMkqcWbz5KkFoNBktRiMEiSWgwGSVLL/wfNZWjztP+jJgAAAABJRU5ErkJggg==\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.barplot(df['price_range'],df['mobile_wt'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='price_range', ylabel='n_cores'>"
      ]
     },
     "execution_count": 84,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.barplot(df['price_range'],df['n_cores'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='price_range', ylabel='n_cores'>"
      ]
     },
     "execution_count": 85,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.boxplot(df['price_range'],df['n_cores'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 87,
   "metadata": {},
   "outputs": [],
   "source": [
    "area=df['sc_h']*df['sc_w']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 88,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0        63\n",
       "1        51\n",
       "2        22\n",
       "3       128\n",
       "4        16\n",
       "       ... \n",
       "1995     52\n",
       "1996    110\n",
       "1997      9\n",
       "1998    180\n",
       "1999     76\n",
       "Length: 2000, dtype: int64"
      ]
     },
     "execution_count": 88,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "area"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Categorical columns:\n",
    "blue\n",
    "clock speed\n",
    "dual sim\n",
    "four_g\n",
    "n_cores\n",
    "three_g\n",
    "touch_screen\n",
    "wifi"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [],
   "source": [
    "matrix = df.corr()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 92,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>battery_power</th>\n",
       "      <th>blue</th>\n",
       "      <th>clock_speed</th>\n",
       "      <th>dual_sim</th>\n",
       "      <th>fc</th>\n",
       "      <th>four_g</th>\n",
       "      <th>int_memory</th>\n",
       "      <th>m_dep</th>\n",
       "      <th>mobile_wt</th>\n",
       "      <th>n_cores</th>\n",
       "      <th>...</th>\n",
       "      <th>px_height</th>\n",
       "      <th>px_width</th>\n",
       "      <th>ram</th>\n",
       "      <th>sc_h</th>\n",
       "      <th>sc_w</th>\n",
       "      <th>talk_time</th>\n",
       "      <th>three_g</th>\n",
       "      <th>touch_screen</th>\n",
       "      <th>wifi</th>\n",
       "      <th>price_range</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>battery_power</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.011252</td>\n",
       "      <td>0.011482</td>\n",
       "      <td>-0.041847</td>\n",
       "      <td>0.033334</td>\n",
       "      <td>0.015665</td>\n",
       "      <td>-0.004004</td>\n",
       "      <td>0.034085</td>\n",
       "      <td>0.001844</td>\n",
       "      <td>-0.029727</td>\n",
       "      <td>...</td>\n",
       "      <td>0.014901</td>\n",
       "      <td>-0.008402</td>\n",
       "      <td>-0.000653</td>\n",
       "      <td>-0.029959</td>\n",
       "      <td>-0.021421</td>\n",
       "      <td>0.052510</td>\n",
       "      <td>0.011522</td>\n",
       "      <td>-0.010516</td>\n",
       "      <td>-0.008343</td>\n",
       "      <td>0.200723</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>blue</th>\n",
       "      <td>0.011252</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.021419</td>\n",
       "      <td>0.035198</td>\n",
       "      <td>0.003593</td>\n",
       "      <td>0.013443</td>\n",
       "      <td>0.041177</td>\n",
       "      <td>0.004049</td>\n",
       "      <td>-0.008605</td>\n",
       "      <td>0.036161</td>\n",
       "      <td>...</td>\n",
       "      <td>-0.006872</td>\n",
       "      <td>-0.041533</td>\n",
       "      <td>0.026351</td>\n",
       "      <td>-0.002952</td>\n",
       "      <td>0.000613</td>\n",
       "      <td>0.013934</td>\n",
       "      <td>-0.030236</td>\n",
       "      <td>0.010061</td>\n",
       "      <td>-0.021863</td>\n",
       "      <td>0.020573</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>clock_speed</th>\n",
       "      <td>0.011482</td>\n",
       "      <td>0.021419</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>-0.001315</td>\n",
       "      <td>-0.000434</td>\n",
       "      <td>-0.043073</td>\n",
       "      <td>0.006545</td>\n",
       "      <td>-0.014364</td>\n",
       "      <td>0.012350</td>\n",
       "      <td>-0.005724</td>\n",
       "      <td>...</td>\n",
       "      <td>-0.014523</td>\n",
       "      <td>-0.009476</td>\n",
       "      <td>0.003443</td>\n",
       "      <td>-0.029078</td>\n",
       "      <td>-0.007378</td>\n",
       "      <td>-0.011432</td>\n",
       "      <td>-0.046433</td>\n",
       "      <td>0.019756</td>\n",
       "      <td>-0.024471</td>\n",
       "      <td>-0.006606</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>dual_sim</th>\n",
       "      <td>-0.041847</td>\n",
       "      <td>0.035198</td>\n",
       "      <td>-0.001315</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>-0.029123</td>\n",
       "      <td>0.003187</td>\n",
       "      <td>-0.015679</td>\n",
       "      <td>-0.022142</td>\n",
       "      <td>-0.008979</td>\n",
       "      <td>-0.024658</td>\n",
       "      <td>...</td>\n",
       "      <td>-0.020875</td>\n",
       "      <td>0.014291</td>\n",
       "      <td>0.041072</td>\n",
       "      <td>-0.011949</td>\n",
       "      <td>-0.016666</td>\n",
       "      <td>-0.039404</td>\n",
       "      <td>-0.014008</td>\n",
       "      <td>-0.017117</td>\n",
       "      <td>0.022740</td>\n",
       "      <td>0.017444</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>fc</th>\n",
       "      <td>0.033334</td>\n",
       "      <td>0.003593</td>\n",
       "      <td>-0.000434</td>\n",
       "      <td>-0.029123</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>-0.016560</td>\n",
       "      <td>-0.029133</td>\n",
       "      <td>-0.001791</td>\n",
       "      <td>0.023618</td>\n",
       "      <td>-0.013356</td>\n",
       "      <td>...</td>\n",
       "      <td>-0.009990</td>\n",
       "      <td>-0.005176</td>\n",
       "      <td>0.015099</td>\n",
       "      <td>-0.011014</td>\n",
       "      <td>-0.012373</td>\n",
       "      <td>-0.006829</td>\n",
       "      <td>0.001793</td>\n",
       "      <td>-0.014828</td>\n",
       "      <td>0.020085</td>\n",
       "      <td>0.021998</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>four_g</th>\n",
       "      <td>0.015665</td>\n",
       "      <td>0.013443</td>\n",
       "      <td>-0.043073</td>\n",
       "      <td>0.003187</td>\n",
       "      <td>-0.016560</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.008690</td>\n",
       "      <td>-0.001823</td>\n",
       "      <td>-0.016537</td>\n",
       "      <td>-0.029706</td>\n",
       "      <td>...</td>\n",
       "      <td>-0.019236</td>\n",
       "      <td>0.007448</td>\n",
       "      <td>0.007313</td>\n",
       "      <td>0.027166</td>\n",
       "      <td>0.037005</td>\n",
       "      <td>-0.046628</td>\n",
       "      <td>0.584246</td>\n",
       "      <td>0.016758</td>\n",
       "      <td>-0.017620</td>\n",
       "      <td>0.014772</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>int_memory</th>\n",
       "      <td>-0.004004</td>\n",
       "      <td>0.041177</td>\n",
       "      <td>0.006545</td>\n",
       "      <td>-0.015679</td>\n",
       "      <td>-0.029133</td>\n",
       "      <td>0.008690</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.006886</td>\n",
       "      <td>-0.034214</td>\n",
       "      <td>-0.028310</td>\n",
       "      <td>...</td>\n",
       "      <td>0.010441</td>\n",
       "      <td>-0.008335</td>\n",
       "      <td>0.032813</td>\n",
       "      <td>0.037771</td>\n",
       "      <td>0.011731</td>\n",
       "      <td>-0.002790</td>\n",
       "      <td>-0.009366</td>\n",
       "      <td>-0.026999</td>\n",
       "      <td>0.006993</td>\n",
       "      <td>0.044435</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>m_dep</th>\n",
       "      <td>0.034085</td>\n",
       "      <td>0.004049</td>\n",
       "      <td>-0.014364</td>\n",
       "      <td>-0.022142</td>\n",
       "      <td>-0.001791</td>\n",
       "      <td>-0.001823</td>\n",
       "      <td>0.006886</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.021756</td>\n",
       "      <td>-0.003504</td>\n",
       "      <td>...</td>\n",
       "      <td>0.025263</td>\n",
       "      <td>0.023566</td>\n",
       "      <td>-0.009434</td>\n",
       "      <td>-0.025348</td>\n",
       "      <td>-0.018388</td>\n",
       "      <td>0.017003</td>\n",
       "      <td>-0.012065</td>\n",
       "      <td>-0.002638</td>\n",
       "      <td>-0.028353</td>\n",
       "      <td>0.000853</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mobile_wt</th>\n",
       "      <td>0.001844</td>\n",
       "      <td>-0.008605</td>\n",
       "      <td>0.012350</td>\n",
       "      <td>-0.008979</td>\n",
       "      <td>0.023618</td>\n",
       "      <td>-0.016537</td>\n",
       "      <td>-0.034214</td>\n",
       "      <td>0.021756</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>-0.018989</td>\n",
       "      <td>...</td>\n",
       "      <td>0.000939</td>\n",
       "      <td>0.000090</td>\n",
       "      <td>-0.002581</td>\n",
       "      <td>-0.033855</td>\n",
       "      <td>-0.020761</td>\n",
       "      <td>0.006209</td>\n",
       "      <td>0.001551</td>\n",
       "      <td>-0.014368</td>\n",
       "      <td>-0.000409</td>\n",
       "      <td>-0.030302</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>n_cores</th>\n",
       "      <td>-0.029727</td>\n",
       "      <td>0.036161</td>\n",
       "      <td>-0.005724</td>\n",
       "      <td>-0.024658</td>\n",
       "      <td>-0.013356</td>\n",
       "      <td>-0.029706</td>\n",
       "      <td>-0.028310</td>\n",
       "      <td>-0.003504</td>\n",
       "      <td>-0.018989</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>...</td>\n",
       "      <td>-0.006872</td>\n",
       "      <td>0.024480</td>\n",
       "      <td>0.004868</td>\n",
       "      <td>-0.000315</td>\n",
       "      <td>0.025826</td>\n",
       "      <td>0.013148</td>\n",
       "      <td>-0.014733</td>\n",
       "      <td>0.023774</td>\n",
       "      <td>-0.009964</td>\n",
       "      <td>0.004399</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>pc</th>\n",
       "      <td>0.031441</td>\n",
       "      <td>-0.009952</td>\n",
       "      <td>-0.005245</td>\n",
       "      <td>-0.017143</td>\n",
       "      <td>0.644595</td>\n",
       "      <td>-0.005598</td>\n",
       "      <td>-0.033273</td>\n",
       "      <td>0.026282</td>\n",
       "      <td>0.018844</td>\n",
       "      <td>-0.001193</td>\n",
       "      <td>...</td>\n",
       "      <td>-0.018465</td>\n",
       "      <td>0.004196</td>\n",
       "      <td>0.028984</td>\n",
       "      <td>0.004938</td>\n",
       "      <td>-0.023819</td>\n",
       "      <td>0.014657</td>\n",
       "      <td>-0.001322</td>\n",
       "      <td>-0.008742</td>\n",
       "      <td>0.005389</td>\n",
       "      <td>0.033599</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>px_height</th>\n",
       "      <td>0.014901</td>\n",
       "      <td>-0.006872</td>\n",
       "      <td>-0.014523</td>\n",
       "      <td>-0.020875</td>\n",
       "      <td>-0.009990</td>\n",
       "      <td>-0.019236</td>\n",
       "      <td>0.010441</td>\n",
       "      <td>0.025263</td>\n",
       "      <td>0.000939</td>\n",
       "      <td>-0.006872</td>\n",
       "      <td>...</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.510664</td>\n",
       "      <td>-0.020352</td>\n",
       "      <td>0.059615</td>\n",
       "      <td>0.043038</td>\n",
       "      <td>-0.010645</td>\n",
       "      <td>-0.031174</td>\n",
       "      <td>0.021891</td>\n",
       "      <td>0.051824</td>\n",
       "      <td>0.148858</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>px_width</th>\n",
       "      <td>-0.008402</td>\n",
       "      <td>-0.041533</td>\n",
       "      <td>-0.009476</td>\n",
       "      <td>0.014291</td>\n",
       "      <td>-0.005176</td>\n",
       "      <td>0.007448</td>\n",
       "      <td>-0.008335</td>\n",
       "      <td>0.023566</td>\n",
       "      <td>0.000090</td>\n",
       "      <td>0.024480</td>\n",
       "      <td>...</td>\n",
       "      <td>0.510664</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.004105</td>\n",
       "      <td>0.021599</td>\n",
       "      <td>0.034699</td>\n",
       "      <td>0.006720</td>\n",
       "      <td>0.000350</td>\n",
       "      <td>-0.001628</td>\n",
       "      <td>0.030319</td>\n",
       "      <td>0.165818</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>ram</th>\n",
       "      <td>-0.000653</td>\n",
       "      <td>0.026351</td>\n",
       "      <td>0.003443</td>\n",
       "      <td>0.041072</td>\n",
       "      <td>0.015099</td>\n",
       "      <td>0.007313</td>\n",
       "      <td>0.032813</td>\n",
       "      <td>-0.009434</td>\n",
       "      <td>-0.002581</td>\n",
       "      <td>0.004868</td>\n",
       "      <td>...</td>\n",
       "      <td>-0.020352</td>\n",
       "      <td>0.004105</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.015996</td>\n",
       "      <td>0.035576</td>\n",
       "      <td>0.010820</td>\n",
       "      <td>0.015795</td>\n",
       "      <td>-0.030455</td>\n",
       "      <td>0.022669</td>\n",
       "      <td>0.917046</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>sc_h</th>\n",
       "      <td>-0.029959</td>\n",
       "      <td>-0.002952</td>\n",
       "      <td>-0.029078</td>\n",
       "      <td>-0.011949</td>\n",
       "      <td>-0.011014</td>\n",
       "      <td>0.027166</td>\n",
       "      <td>0.037771</td>\n",
       "      <td>-0.025348</td>\n",
       "      <td>-0.033855</td>\n",
       "      <td>-0.000315</td>\n",
       "      <td>...</td>\n",
       "      <td>0.059615</td>\n",
       "      <td>0.021599</td>\n",
       "      <td>0.015996</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.506144</td>\n",
       "      <td>-0.017335</td>\n",
       "      <td>0.012033</td>\n",
       "      <td>-0.020023</td>\n",
       "      <td>0.025929</td>\n",
       "      <td>0.022986</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>sc_w</th>\n",
       "      <td>-0.021421</td>\n",
       "      <td>0.000613</td>\n",
       "      <td>-0.007378</td>\n",
       "      <td>-0.016666</td>\n",
       "      <td>-0.012373</td>\n",
       "      <td>0.037005</td>\n",
       "      <td>0.011731</td>\n",
       "      <td>-0.018388</td>\n",
       "      <td>-0.020761</td>\n",
       "      <td>0.025826</td>\n",
       "      <td>...</td>\n",
       "      <td>0.043038</td>\n",
       "      <td>0.034699</td>\n",
       "      <td>0.035576</td>\n",
       "      <td>0.506144</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>-0.022821</td>\n",
       "      <td>0.030941</td>\n",
       "      <td>0.012720</td>\n",
       "      <td>0.035423</td>\n",
       "      <td>0.038711</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>talk_time</th>\n",
       "      <td>0.052510</td>\n",
       "      <td>0.013934</td>\n",
       "      <td>-0.011432</td>\n",
       "      <td>-0.039404</td>\n",
       "      <td>-0.006829</td>\n",
       "      <td>-0.046628</td>\n",
       "      <td>-0.002790</td>\n",
       "      <td>0.017003</td>\n",
       "      <td>0.006209</td>\n",
       "      <td>0.013148</td>\n",
       "      <td>...</td>\n",
       "      <td>-0.010645</td>\n",
       "      <td>0.006720</td>\n",
       "      <td>0.010820</td>\n",
       "      <td>-0.017335</td>\n",
       "      <td>-0.022821</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>-0.042688</td>\n",
       "      <td>0.017196</td>\n",
       "      <td>-0.029504</td>\n",
       "      <td>0.021859</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>three_g</th>\n",
       "      <td>0.011522</td>\n",
       "      <td>-0.030236</td>\n",
       "      <td>-0.046433</td>\n",
       "      <td>-0.014008</td>\n",
       "      <td>0.001793</td>\n",
       "      <td>0.584246</td>\n",
       "      <td>-0.009366</td>\n",
       "      <td>-0.012065</td>\n",
       "      <td>0.001551</td>\n",
       "      <td>-0.014733</td>\n",
       "      <td>...</td>\n",
       "      <td>-0.031174</td>\n",
       "      <td>0.000350</td>\n",
       "      <td>0.015795</td>\n",
       "      <td>0.012033</td>\n",
       "      <td>0.030941</td>\n",
       "      <td>-0.042688</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.013917</td>\n",
       "      <td>0.004316</td>\n",
       "      <td>0.023611</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>touch_screen</th>\n",
       "      <td>-0.010516</td>\n",
       "      <td>0.010061</td>\n",
       "      <td>0.019756</td>\n",
       "      <td>-0.017117</td>\n",
       "      <td>-0.014828</td>\n",
       "      <td>0.016758</td>\n",
       "      <td>-0.026999</td>\n",
       "      <td>-0.002638</td>\n",
       "      <td>-0.014368</td>\n",
       "      <td>0.023774</td>\n",
       "      <td>...</td>\n",
       "      <td>0.021891</td>\n",
       "      <td>-0.001628</td>\n",
       "      <td>-0.030455</td>\n",
       "      <td>-0.020023</td>\n",
       "      <td>0.012720</td>\n",
       "      <td>0.017196</td>\n",
       "      <td>0.013917</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.011917</td>\n",
       "      <td>-0.030411</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>wifi</th>\n",
       "      <td>-0.008343</td>\n",
       "      <td>-0.021863</td>\n",
       "      <td>-0.024471</td>\n",
       "      <td>0.022740</td>\n",
       "      <td>0.020085</td>\n",
       "      <td>-0.017620</td>\n",
       "      <td>0.006993</td>\n",
       "      <td>-0.028353</td>\n",
       "      <td>-0.000409</td>\n",
       "      <td>-0.009964</td>\n",
       "      <td>...</td>\n",
       "      <td>0.051824</td>\n",
       "      <td>0.030319</td>\n",
       "      <td>0.022669</td>\n",
       "      <td>0.025929</td>\n",
       "      <td>0.035423</td>\n",
       "      <td>-0.029504</td>\n",
       "      <td>0.004316</td>\n",
       "      <td>0.011917</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.018785</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>price_range</th>\n",
       "      <td>0.200723</td>\n",
       "      <td>0.020573</td>\n",
       "      <td>-0.006606</td>\n",
       "      <td>0.017444</td>\n",
       "      <td>0.021998</td>\n",
       "      <td>0.014772</td>\n",
       "      <td>0.044435</td>\n",
       "      <td>0.000853</td>\n",
       "      <td>-0.030302</td>\n",
       "      <td>0.004399</td>\n",
       "      <td>...</td>\n",
       "      <td>0.148858</td>\n",
       "      <td>0.165818</td>\n",
       "      <td>0.917046</td>\n",
       "      <td>0.022986</td>\n",
       "      <td>0.038711</td>\n",
       "      <td>0.021859</td>\n",
       "      <td>0.023611</td>\n",
       "      <td>-0.030411</td>\n",
       "      <td>0.018785</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>21 rows × 21 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "               battery_power      blue  clock_speed  dual_sim        fc  \\\n",
       "battery_power       1.000000  0.011252     0.011482 -0.041847  0.033334   \n",
       "blue                0.011252  1.000000     0.021419  0.035198  0.003593   \n",
       "clock_speed         0.011482  0.021419     1.000000 -0.001315 -0.000434   \n",
       "dual_sim           -0.041847  0.035198    -0.001315  1.000000 -0.029123   \n",
       "fc                  0.033334  0.003593    -0.000434 -0.029123  1.000000   \n",
       "four_g              0.015665  0.013443    -0.043073  0.003187 -0.016560   \n",
       "int_memory         -0.004004  0.041177     0.006545 -0.015679 -0.029133   \n",
       "m_dep               0.034085  0.004049    -0.014364 -0.022142 -0.001791   \n",
       "mobile_wt           0.001844 -0.008605     0.012350 -0.008979  0.023618   \n",
       "n_cores            -0.029727  0.036161    -0.005724 -0.024658 -0.013356   \n",
       "pc                  0.031441 -0.009952    -0.005245 -0.017143  0.644595   \n",
       "px_height           0.014901 -0.006872    -0.014523 -0.020875 -0.009990   \n",
       "px_width           -0.008402 -0.041533    -0.009476  0.014291 -0.005176   \n",
       "ram                -0.000653  0.026351     0.003443  0.041072  0.015099   \n",
       "sc_h               -0.029959 -0.002952    -0.029078 -0.011949 -0.011014   \n",
       "sc_w               -0.021421  0.000613    -0.007378 -0.016666 -0.012373   \n",
       "talk_time           0.052510  0.013934    -0.011432 -0.039404 -0.006829   \n",
       "three_g             0.011522 -0.030236    -0.046433 -0.014008  0.001793   \n",
       "touch_screen       -0.010516  0.010061     0.019756 -0.017117 -0.014828   \n",
       "wifi               -0.008343 -0.021863    -0.024471  0.022740  0.020085   \n",
       "price_range         0.200723  0.020573    -0.006606  0.017444  0.021998   \n",
       "\n",
       "                 four_g  int_memory     m_dep  mobile_wt   n_cores  ...  \\\n",
       "battery_power  0.015665   -0.004004  0.034085   0.001844 -0.029727  ...   \n",
       "blue           0.013443    0.041177  0.004049  -0.008605  0.036161  ...   \n",
       "clock_speed   -0.043073    0.006545 -0.014364   0.012350 -0.005724  ...   \n",
       "dual_sim       0.003187   -0.015679 -0.022142  -0.008979 -0.024658  ...   \n",
       "fc            -0.016560   -0.029133 -0.001791   0.023618 -0.013356  ...   \n",
       "four_g         1.000000    0.008690 -0.001823  -0.016537 -0.029706  ...   \n",
       "int_memory     0.008690    1.000000  0.006886  -0.034214 -0.028310  ...   \n",
       "m_dep         -0.001823    0.006886  1.000000   0.021756 -0.003504  ...   \n",
       "mobile_wt     -0.016537   -0.034214  0.021756   1.000000 -0.018989  ...   \n",
       "n_cores       -0.029706   -0.028310 -0.003504  -0.018989  1.000000  ...   \n",
       "pc            -0.005598   -0.033273  0.026282   0.018844 -0.001193  ...   \n",
       "px_height     -0.019236    0.010441  0.025263   0.000939 -0.006872  ...   \n",
       "px_width       0.007448   -0.008335  0.023566   0.000090  0.024480  ...   \n",
       "ram            0.007313    0.032813 -0.009434  -0.002581  0.004868  ...   \n",
       "sc_h           0.027166    0.037771 -0.025348  -0.033855 -0.000315  ...   \n",
       "sc_w           0.037005    0.011731 -0.018388  -0.020761  0.025826  ...   \n",
       "talk_time     -0.046628   -0.002790  0.017003   0.006209  0.013148  ...   \n",
       "three_g        0.584246   -0.009366 -0.012065   0.001551 -0.014733  ...   \n",
       "touch_screen   0.016758   -0.026999 -0.002638  -0.014368  0.023774  ...   \n",
       "wifi          -0.017620    0.006993 -0.028353  -0.000409 -0.009964  ...   \n",
       "price_range    0.014772    0.044435  0.000853  -0.030302  0.004399  ...   \n",
       "\n",
       "               px_height  px_width       ram      sc_h      sc_w  talk_time  \\\n",
       "battery_power   0.014901 -0.008402 -0.000653 -0.029959 -0.021421   0.052510   \n",
       "blue           -0.006872 -0.041533  0.026351 -0.002952  0.000613   0.013934   \n",
       "clock_speed    -0.014523 -0.009476  0.003443 -0.029078 -0.007378  -0.011432   \n",
       "dual_sim       -0.020875  0.014291  0.041072 -0.011949 -0.016666  -0.039404   \n",
       "fc             -0.009990 -0.005176  0.015099 -0.011014 -0.012373  -0.006829   \n",
       "four_g         -0.019236  0.007448  0.007313  0.027166  0.037005  -0.046628   \n",
       "int_memory      0.010441 -0.008335  0.032813  0.037771  0.011731  -0.002790   \n",
       "m_dep           0.025263  0.023566 -0.009434 -0.025348 -0.018388   0.017003   \n",
       "mobile_wt       0.000939  0.000090 -0.002581 -0.033855 -0.020761   0.006209   \n",
       "n_cores        -0.006872  0.024480  0.004868 -0.000315  0.025826   0.013148   \n",
       "pc             -0.018465  0.004196  0.028984  0.004938 -0.023819   0.014657   \n",
       "px_height       1.000000  0.510664 -0.020352  0.059615  0.043038  -0.010645   \n",
       "px_width        0.510664  1.000000  0.004105  0.021599  0.034699   0.006720   \n",
       "ram            -0.020352  0.004105  1.000000  0.015996  0.035576   0.010820   \n",
       "sc_h            0.059615  0.021599  0.015996  1.000000  0.506144  -0.017335   \n",
       "sc_w            0.043038  0.034699  0.035576  0.506144  1.000000  -0.022821   \n",
       "talk_time      -0.010645  0.006720  0.010820 -0.017335 -0.022821   1.000000   \n",
       "three_g        -0.031174  0.000350  0.015795  0.012033  0.030941  -0.042688   \n",
       "touch_screen    0.021891 -0.001628 -0.030455 -0.020023  0.012720   0.017196   \n",
       "wifi            0.051824  0.030319  0.022669  0.025929  0.035423  -0.029504   \n",
       "price_range     0.148858  0.165818  0.917046  0.022986  0.038711   0.021859   \n",
       "\n",
       "                three_g  touch_screen      wifi  price_range  \n",
       "battery_power  0.011522     -0.010516 -0.008343     0.200723  \n",
       "blue          -0.030236      0.010061 -0.021863     0.020573  \n",
       "clock_speed   -0.046433      0.019756 -0.024471    -0.006606  \n",
       "dual_sim      -0.014008     -0.017117  0.022740     0.017444  \n",
       "fc             0.001793     -0.014828  0.020085     0.021998  \n",
       "four_g         0.584246      0.016758 -0.017620     0.014772  \n",
       "int_memory    -0.009366     -0.026999  0.006993     0.044435  \n",
       "m_dep         -0.012065     -0.002638 -0.028353     0.000853  \n",
       "mobile_wt      0.001551     -0.014368 -0.000409    -0.030302  \n",
       "n_cores       -0.014733      0.023774 -0.009964     0.004399  \n",
       "pc            -0.001322     -0.008742  0.005389     0.033599  \n",
       "px_height     -0.031174      0.021891  0.051824     0.148858  \n",
       "px_width       0.000350     -0.001628  0.030319     0.165818  \n",
       "ram            0.015795     -0.030455  0.022669     0.917046  \n",
       "sc_h           0.012033     -0.020023  0.025929     0.022986  \n",
       "sc_w           0.030941      0.012720  0.035423     0.038711  \n",
       "talk_time     -0.042688      0.017196 -0.029504     0.021859  \n",
       "three_g        1.000000      0.013917  0.004316     0.023611  \n",
       "touch_screen   0.013917      1.000000  0.011917    -0.030411  \n",
       "wifi           0.004316      0.011917  1.000000     0.018785  \n",
       "price_range    0.023611     -0.030411  0.018785     1.000000  \n",
       "\n",
       "[21 rows x 21 columns]"
      ]
     },
     "execution_count": 92,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "matrix"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 936x720 with 2 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.subplots(figsize=(13,10))\n",
    "sns.heatmap(matrix,vmax=0.8,square=True,cmap='BuPu');"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.preprocessing import StandardScaler"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 104,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.naive_bayes import GaussianNB\n",
    "from sklearn.naive_bayes import MultinomialNB\n",
    "from sklearn.linear_model import LinearRegression\n",
    "from sklearn.neighbors import KNeighborsClassifier\n",
    "from sklearn.linear_model import LogisticRegression\n",
    "from sklearn.tree import DecisionTreeClassifier\n",
    "from sklearn.svm import SVC\n",
    "from sklearn.ensemble import RandomForestClassifier\n",
    "from sklearn.neighbors import KNeighborsClassifier\n",
    "from sklearn.ensemble import GradientBoostingClassifier\n",
    "\n",
    "from sklearn.metrics import accuracy_score\n",
    "from sklearn.metrics import classification_report\n",
    "from sklearn.metrics import confusion_matrix"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [],
   "source": [
    "X=df.drop('price_range',1)\n",
    "y = df['price_range']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 109,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>battery_power</th>\n",
       "      <th>blue</th>\n",
       "      <th>clock_speed</th>\n",
       "      <th>dual_sim</th>\n",
       "      <th>fc</th>\n",
       "      <th>four_g</th>\n",
       "      <th>int_memory</th>\n",
       "      <th>m_dep</th>\n",
       "      <th>mobile_wt</th>\n",
       "      <th>n_cores</th>\n",
       "      <th>pc</th>\n",
       "      <th>px_height</th>\n",
       "      <th>px_width</th>\n",
       "      <th>ram</th>\n",
       "      <th>sc_h</th>\n",
       "      <th>sc_w</th>\n",
       "      <th>talk_time</th>\n",
       "      <th>three_g</th>\n",
       "      <th>touch_screen</th>\n",
       "      <th>wifi</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>968</th>\n",
       "      <td>1923</td>\n",
       "      <td>0</td>\n",
       "      <td>0.5</td>\n",
       "      <td>1</td>\n",
       "      <td>7</td>\n",
       "      <td>0</td>\n",
       "      <td>46</td>\n",
       "      <td>0.5</td>\n",
       "      <td>191</td>\n",
       "      <td>1</td>\n",
       "      <td>10</td>\n",
       "      <td>767</td>\n",
       "      <td>1759</td>\n",
       "      <td>1489</td>\n",
       "      <td>10</td>\n",
       "      <td>9</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>240</th>\n",
       "      <td>633</td>\n",
       "      <td>1</td>\n",
       "      <td>2.2</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>49</td>\n",
       "      <td>0.1</td>\n",
       "      <td>139</td>\n",
       "      <td>8</td>\n",
       "      <td>1</td>\n",
       "      <td>529</td>\n",
       "      <td>1009</td>\n",
       "      <td>3560</td>\n",
       "      <td>11</td>\n",
       "      <td>1</td>\n",
       "      <td>16</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>819</th>\n",
       "      <td>1236</td>\n",
       "      <td>0</td>\n",
       "      <td>0.9</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>57</td>\n",
       "      <td>0.1</td>\n",
       "      <td>188</td>\n",
       "      <td>1</td>\n",
       "      <td>14</td>\n",
       "      <td>517</td>\n",
       "      <td>809</td>\n",
       "      <td>1406</td>\n",
       "      <td>14</td>\n",
       "      <td>12</td>\n",
       "      <td>20</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>692</th>\n",
       "      <td>781</td>\n",
       "      <td>0</td>\n",
       "      <td>1.1</td>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "      <td>38</td>\n",
       "      <td>0.4</td>\n",
       "      <td>198</td>\n",
       "      <td>5</td>\n",
       "      <td>7</td>\n",
       "      <td>304</td>\n",
       "      <td>1674</td>\n",
       "      <td>3508</td>\n",
       "      <td>13</td>\n",
       "      <td>8</td>\n",
       "      <td>5</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>420</th>\n",
       "      <td>1456</td>\n",
       "      <td>1</td>\n",
       "      <td>0.5</td>\n",
       "      <td>1</td>\n",
       "      <td>7</td>\n",
       "      <td>0</td>\n",
       "      <td>7</td>\n",
       "      <td>0.4</td>\n",
       "      <td>105</td>\n",
       "      <td>5</td>\n",
       "      <td>12</td>\n",
       "      <td>823</td>\n",
       "      <td>1104</td>\n",
       "      <td>1587</td>\n",
       "      <td>6</td>\n",
       "      <td>5</td>\n",
       "      <td>20</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1130</th>\n",
       "      <td>1975</td>\n",
       "      <td>1</td>\n",
       "      <td>1.9</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "      <td>31</td>\n",
       "      <td>0.9</td>\n",
       "      <td>151</td>\n",
       "      <td>1</td>\n",
       "      <td>17</td>\n",
       "      <td>775</td>\n",
       "      <td>1607</td>\n",
       "      <td>3022</td>\n",
       "      <td>13</td>\n",
       "      <td>5</td>\n",
       "      <td>19</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1294</th>\n",
       "      <td>589</td>\n",
       "      <td>1</td>\n",
       "      <td>0.5</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>59</td>\n",
       "      <td>0.7</td>\n",
       "      <td>146</td>\n",
       "      <td>8</td>\n",
       "      <td>4</td>\n",
       "      <td>759</td>\n",
       "      <td>1858</td>\n",
       "      <td>362</td>\n",
       "      <td>16</td>\n",
       "      <td>10</td>\n",
       "      <td>6</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>860</th>\n",
       "      <td>1829</td>\n",
       "      <td>1</td>\n",
       "      <td>0.5</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>15</td>\n",
       "      <td>0.4</td>\n",
       "      <td>160</td>\n",
       "      <td>5</td>\n",
       "      <td>7</td>\n",
       "      <td>729</td>\n",
       "      <td>1267</td>\n",
       "      <td>2080</td>\n",
       "      <td>16</td>\n",
       "      <td>11</td>\n",
       "      <td>12</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1459</th>\n",
       "      <td>1927</td>\n",
       "      <td>0</td>\n",
       "      <td>0.9</td>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>0</td>\n",
       "      <td>11</td>\n",
       "      <td>0.4</td>\n",
       "      <td>190</td>\n",
       "      <td>8</td>\n",
       "      <td>12</td>\n",
       "      <td>491</td>\n",
       "      <td>1506</td>\n",
       "      <td>2916</td>\n",
       "      <td>16</td>\n",
       "      <td>11</td>\n",
       "      <td>18</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1126</th>\n",
       "      <td>635</td>\n",
       "      <td>1</td>\n",
       "      <td>0.6</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>50</td>\n",
       "      <td>0.3</td>\n",
       "      <td>97</td>\n",
       "      <td>5</td>\n",
       "      <td>13</td>\n",
       "      <td>193</td>\n",
       "      <td>989</td>\n",
       "      <td>2107</td>\n",
       "      <td>13</td>\n",
       "      <td>12</td>\n",
       "      <td>12</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>1600 rows × 20 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "      battery_power  blue  clock_speed  dual_sim  fc  four_g  int_memory  \\\n",
       "968            1923     0          0.5         1   7       0          46   \n",
       "240             633     1          2.2         0   0       1          49   \n",
       "819            1236     0          0.9         1   2       1          57   \n",
       "692             781     0          1.1         0   2       0          38   \n",
       "420            1456     1          0.5         1   7       0           7   \n",
       "...             ...   ...          ...       ...  ..     ...         ...   \n",
       "1130           1975     1          1.9         1   2       0          31   \n",
       "1294            589     1          0.5         0   1       1          59   \n",
       "860            1829     1          0.5         0   0       1          15   \n",
       "1459           1927     0          0.9         1   3       0          11   \n",
       "1126            635     1          0.6         1   1       1          50   \n",
       "\n",
       "      m_dep  mobile_wt  n_cores  pc  px_height  px_width   ram  sc_h  sc_w  \\\n",
       "968     0.5        191        1  10        767      1759  1489    10     9   \n",
       "240     0.1        139        8   1        529      1009  3560    11     1   \n",
       "819     0.1        188        1  14        517       809  1406    14    12   \n",
       "692     0.4        198        5   7        304      1674  3508    13     8   \n",
       "420     0.4        105        5  12        823      1104  1587     6     5   \n",
       "...     ...        ...      ...  ..        ...       ...   ...   ...   ...   \n",
       "1130    0.9        151        1  17        775      1607  3022    13     5   \n",
       "1294    0.7        146        8   4        759      1858   362    16    10   \n",
       "860     0.4        160        5   7        729      1267  2080    16    11   \n",
       "1459    0.4        190        8  12        491      1506  2916    16    11   \n",
       "1126    0.3         97        5  13        193       989  2107    13    12   \n",
       "\n",
       "      talk_time  three_g  touch_screen  wifi  \n",
       "968           3        1             1     1  \n",
       "240          16        1             1     1  \n",
       "819          20        1             0     1  \n",
       "692           5        0             0     1  \n",
       "420          20        1             0     1  \n",
       "...         ...      ...           ...   ...  \n",
       "1130         19        0             0     1  \n",
       "1294          6        1             1     1  \n",
       "860          12        1             0     1  \n",
       "1459         18        0             1     1  \n",
       "1126         12        1             0     0  \n",
       "\n",
       "[1600 rows x 20 columns]"
      ]
     },
     "execution_count": 109,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x_train, x_cv, y_train, y_cv = train_test_split(X,y,test_size=0.2,random_state=42)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 120,
   "metadata": {},
   "outputs": [],
   "source": [
    "sc = StandardScaler()\n",
    "x_train = sc.fit_transform(x_train)\n",
    "x_cv = sc.fit_transform(x_cv)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 121,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[ 1.54835969, -0.98142253, -1.23622976, ...,  0.55713671,\n",
       "         0.9900495 ,  1.00250313],\n",
       "       [-1.3795348 ,  1.01892912,  0.83711156, ...,  0.55713671,\n",
       "         0.9900495 ,  1.00250313],\n",
       "       [-0.01091435, -0.98142253, -0.74838475, ...,  0.55713671,\n",
       "        -1.0100505 ,  1.00250313],\n",
       "       ...,\n",
       "       [ 1.33500924,  1.01892912, -1.23622976, ...,  0.55713671,\n",
       "        -1.0100505 ,  1.00250313],\n",
       "       [ 1.55743843, -0.98142253, -0.74838475, ..., -1.79489161,\n",
       "         0.9900495 ,  1.00250313],\n",
       "       [-1.37499543,  1.01892912, -1.11426851, ...,  0.55713671,\n",
       "        -1.0100505 , -0.99750312]])"
      ]
     },
     "execution_count": 121,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x_train"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 161,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Accuracy of Logistic Regression:  95.25\n",
      "              precision    recall  f1-score   support\n",
      "\n",
      "           0       1.00      0.98      0.99       107\n",
      "           1       0.98      0.92      0.95        97\n",
      "           2       0.90      0.91      0.91        91\n",
      "           3       0.93      0.99      0.96       105\n",
      "\n",
      "    accuracy                           0.95       400\n",
      "   macro avg       0.95      0.95      0.95       400\n",
      "weighted avg       0.95      0.95      0.95       400\n",
      "\n",
      "[[105   0   0   0]\n",
      " [  2  89   0   0]\n",
      " [  0   8  83   1]\n",
      " [  0   0   8 104]]\n"
     ]
    }
   ],
   "source": [
    "model = LogisticRegression()\n",
    "model.fit(x_train,y_train)\n",
    "pred=model.predict(x_cv)\n",
    "print('Accuracy of Logistic Regression: ',accuracy_score(y_cv,pred)*100)\n",
    "\n",
    "print(classification_report(pred,y_cv))\n",
    "print(confusion_matrix(y_cv,pred))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 101,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Accuracy of Linear Regression:  92.00745047335323\n"
     ]
    }
   ],
   "source": [
    "model = LinearRegression()\n",
    "model.fit(x_train,y_train)\n",
    "pred=model.predict(x_cv)\n",
    "print('Accuracy of Linear Regression: ',model.score(x_cv,y_cv)*100)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Accuracy of KNeighborsClassifier:  55.50000000000001\n",
      "              precision    recall  f1-score   support\n",
      "\n",
      "           0       0.77      0.68      0.72       120\n",
      "           1       0.42      0.40      0.41        95\n",
      "           2       0.43      0.38      0.41       105\n",
      "           3       0.56      0.79      0.66        80\n",
      "\n",
      "    accuracy                           0.56       400\n",
      "   macro avg       0.55      0.56      0.55       400\n",
      "weighted avg       0.56      0.56      0.55       400\n",
      "\n",
      "[[81 20  4  0]\n",
      " [28 38 22  3]\n",
      " [10 28 40 14]\n",
      " [ 1  9 39 63]]\n"
     ]
    }
   ],
   "source": [
    "model = KNeighborsClassifier(n_neighbors=10)\n",
    "model.fit(x_train,y_train)\n",
    "pred=model.predict(x_cv)\n",
    "print('Accuracy of KNeighborsClassifier: ',accuracy_score(y_cv,pred)*100)\n",
    "\n",
    "print(classification_report(pred,y_cv))\n",
    "print(confusion_matrix(y_cv,pred))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 90,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Accuracy of DecisionTreeClassifier:  84.0\n",
      "              precision    recall  f1-score   support\n",
      "\n",
      "           0       0.88      0.94      0.91        98\n",
      "           1       0.90      0.73      0.81       112\n",
      "           2       0.73      0.78      0.75        86\n",
      "           3       0.85      0.91      0.88       104\n",
      "\n",
      "    accuracy                           0.84       400\n",
      "   macro avg       0.84      0.84      0.84       400\n",
      "weighted avg       0.84      0.84      0.84       400\n",
      "\n",
      "[[92 13  0  0]\n",
      " [ 6 82  3  0]\n",
      " [ 0 16 67  9]\n",
      " [ 0  1 16 95]]\n"
     ]
    }
   ],
   "source": [
    "model = DecisionTreeClassifier()\n",
    "model.fit(x_train,y_train)\n",
    "pred=model.predict(x_cv)\n",
    "print('Accuracy of DecisionTreeClassifier: ',model.score(x_cv,y_cv)*100)\n",
    "\n",
    "print(classification_report(pred,y_cv))\n",
    "print(confusion_matrix(y_cv,pred))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 91,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Accuracy of RandomForestClassifier:  88.0\n",
      "              precision    recall  f1-score   support\n",
      "\n",
      "           0       0.96      0.94      0.95       107\n",
      "           1       0.87      0.86      0.86        92\n",
      "           2       0.83      0.78      0.80        98\n",
      "           3       0.86      0.93      0.89       103\n",
      "\n",
      "    accuracy                           0.88       400\n",
      "   macro avg       0.88      0.88      0.88       400\n",
      "weighted avg       0.88      0.88      0.88       400\n",
      "\n",
      "[[101   4   0   0]\n",
      " [  6  79   6   0]\n",
      " [  0   9  76   7]\n",
      " [  0   0  16  96]]\n"
     ]
    }
   ],
   "source": [
    "model = RandomForestClassifier()\n",
    "model.fit(x_train,y_train)\n",
    "pred=model.predict(x_cv)\n",
    "print('Accuracy of RandomForestClassifier: ',model.score(x_cv,y_cv)*100)\n",
    "\n",
    "print(classification_report(pred,y_cv))\n",
    "print(confusion_matrix(y_cv,pred))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 93,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Accuracy of Support Vector Machine:  88.25\n",
      "              precision    recall  f1-score   support\n",
      "\n",
      "           0       0.95      0.93      0.94       108\n",
      "           1       0.89      0.81      0.85       100\n",
      "           2       0.80      0.82      0.81        90\n",
      "           3       0.88      0.96      0.92       102\n",
      "\n",
      "    accuracy                           0.88       400\n",
      "   macro avg       0.88      0.88      0.88       400\n",
      "weighted avg       0.88      0.88      0.88       400\n",
      "\n",
      "[[100   5   0   0]\n",
      " [  8  81   2   0]\n",
      " [  0  14  74   4]\n",
      " [  0   0  14  98]]\n"
     ]
    }
   ],
   "source": [
    "model = SVC()\n",
    "model.fit(x_train,y_train)\n",
    "pred=model.predict(x_cv)\n",
    "print('Accuracy of Support Vector Machine: ',model.score(x_cv,y_cv)*100)\n",
    "\n",
    "print(classification_report(pred,y_cv))\n",
    "print(confusion_matrix(y_cv,pred))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 94,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Accuracy of Gaussian Naive Bayes:  80.5\n",
      "              precision    recall  f1-score   support\n",
      "\n",
      "           0       0.95      0.89      0.92       112\n",
      "           1       0.68      0.79      0.73        78\n",
      "           2       0.77      0.64      0.70       111\n",
      "           3       0.79      0.90      0.84        99\n",
      "\n",
      "    accuracy                           0.81       400\n",
      "   macro avg       0.80      0.81      0.80       400\n",
      "weighted avg       0.81      0.81      0.80       400\n",
      "\n",
      "[[100   5   0   0]\n",
      " [ 12  62  17   0]\n",
      " [  0  11  71  10]\n",
      " [  0   0  23  89]]\n"
     ]
    }
   ],
   "source": [
    "model = GaussianNB()\n",
    "model.fit(x_train,y_train)\n",
    "pred=model.predict(x_cv)\n",
    "print('Accuracy of Gaussian Naive Bayes: ',model.score(x_cv,y_cv)*100)\n",
    "\n",
    "print(classification_report(pred,y_cv))\n",
    "print(confusion_matrix(y_cv,pred))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 96,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Accuracy of  Bernoulli Naive Bayes:  58.25\n",
      "              precision    recall  f1-score   support\n",
      "\n",
      "           0       0.68      0.65      0.66       110\n",
      "           1       0.38      0.44      0.41        79\n",
      "           2       0.60      0.50      0.55       109\n",
      "           3       0.64      0.71      0.67       102\n",
      "\n",
      "    accuracy                           0.58       400\n",
      "   macro avg       0.58      0.57      0.57       400\n",
      "weighted avg       0.59      0.58      0.58       400\n",
      "\n",
      "[[71 34  0  0]\n",
      " [38 35 14  4]\n",
      " [ 1 10 55 26]\n",
      " [ 0  0 40 72]]\n"
     ]
    }
   ],
   "source": [
    "model =  BernoulliNB()\n",
    "model.fit(x_train,y_train)\n",
    "pred=model.predict(x_cv)\n",
    "print('Accuracy of  Bernoulli Naive Bayes: ',model.score(x_cv,y_cv)*100)\n",
    "\n",
    "print(classification_report(pred,y_cv))\n",
    "print(confusion_matrix(y_cv,pred))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 97,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Accuracy of  GradientBoostingClassifier:  90.25\n",
      "              precision    recall  f1-score   support\n",
      "\n",
      "           0       0.97      0.97      0.97       105\n",
      "           1       0.93      0.88      0.90        97\n",
      "           2       0.85      0.80      0.83        97\n",
      "           3       0.86      0.95      0.90       101\n",
      "\n",
      "    accuracy                           0.90       400\n",
      "   macro avg       0.90      0.90      0.90       400\n",
      "weighted avg       0.90      0.90      0.90       400\n",
      "\n",
      "[[102   3   0   0]\n",
      " [  3  85   3   0]\n",
      " [  0   9  78   5]\n",
      " [  0   0  16  96]]\n"
     ]
    }
   ],
   "source": [
    "model =  GradientBoostingClassifier()\n",
    "model.fit(x_train,y_train)\n",
    "pred=model.predict(x_cv)\n",
    "print('Accuracy of  GradientBoostingClassifier: ',model.score(x_cv,y_cv)*100)\n",
    "\n",
    "print(classification_report(pred,y_cv))\n",
    "print(confusion_matrix(y_cv,pred))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 103,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Accuracy of  GradientBoostingClassifier:  76.25\n",
      "              precision    recall  f1-score   support\n",
      "\n",
      "           0       0.94      0.99      0.97       100\n",
      "           1       0.49      0.54      0.51        84\n",
      "           2       0.62      0.51      0.56       112\n",
      "           3       0.93      1.00      0.96       104\n",
      "\n",
      "    accuracy                           0.76       400\n",
      "   macro avg       0.75      0.76      0.75       400\n",
      "weighted avg       0.75      0.76      0.76       400\n",
      "\n",
      "[[ 99   3   3   0]\n",
      " [  1  45  45   0]\n",
      " [  0  35  57   0]\n",
      " [  0   1   7 104]]\n"
     ]
    }
   ],
   "source": [
    "from sklearn.linear_model import SGDClassifier\n",
    "model =  SGDClassifier(max_iter=5000, random_state=0)\n",
    "model.fit(x_train,y_train)\n",
    "pred=model.predict(x_cv)\n",
    "print('Accuracy of  GradientBoostingClassifier: ',model.score(x_cv,y_cv)*100)\n",
    "\n",
    "print(classification_report(pred,y_cv))\n",
    "print(confusion_matrix(y_cv,pred))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 106,
   "metadata": {},
   "outputs": [],
   "source": [
    "df_test = pd.read_csv('test.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 110,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>id</th>\n",
       "      <th>battery_power</th>\n",
       "      <th>blue</th>\n",
       "      <th>clock_speed</th>\n",
       "      <th>dual_sim</th>\n",
       "      <th>fc</th>\n",
       "      <th>four_g</th>\n",
       "      <th>int_memory</th>\n",
       "      <th>m_dep</th>\n",
       "      <th>mobile_wt</th>\n",
       "      <th>...</th>\n",
       "      <th>pc</th>\n",
       "      <th>px_height</th>\n",
       "      <th>px_width</th>\n",
       "      <th>ram</th>\n",
       "      <th>sc_h</th>\n",
       "      <th>sc_w</th>\n",
       "      <th>talk_time</th>\n",
       "      <th>three_g</th>\n",
       "      <th>touch_screen</th>\n",
       "      <th>wifi</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>1043</td>\n",
       "      <td>1</td>\n",
       "      <td>1.8</td>\n",
       "      <td>1</td>\n",
       "      <td>14</td>\n",
       "      <td>0</td>\n",
       "      <td>5</td>\n",
       "      <td>0.1</td>\n",
       "      <td>193</td>\n",
       "      <td>...</td>\n",
       "      <td>16</td>\n",
       "      <td>226</td>\n",
       "      <td>1412</td>\n",
       "      <td>3476</td>\n",
       "      <td>12</td>\n",
       "      <td>7</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>841</td>\n",
       "      <td>1</td>\n",
       "      <td>0.5</td>\n",
       "      <td>1</td>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "      <td>61</td>\n",
       "      <td>0.8</td>\n",
       "      <td>191</td>\n",
       "      <td>...</td>\n",
       "      <td>12</td>\n",
       "      <td>746</td>\n",
       "      <td>857</td>\n",
       "      <td>3895</td>\n",
       "      <td>6</td>\n",
       "      <td>0</td>\n",
       "      <td>7</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>1807</td>\n",
       "      <td>1</td>\n",
       "      <td>2.8</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>27</td>\n",
       "      <td>0.9</td>\n",
       "      <td>186</td>\n",
       "      <td>...</td>\n",
       "      <td>4</td>\n",
       "      <td>1270</td>\n",
       "      <td>1366</td>\n",
       "      <td>2396</td>\n",
       "      <td>17</td>\n",
       "      <td>10</td>\n",
       "      <td>10</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>1546</td>\n",
       "      <td>0</td>\n",
       "      <td>0.5</td>\n",
       "      <td>1</td>\n",
       "      <td>18</td>\n",
       "      <td>1</td>\n",
       "      <td>25</td>\n",
       "      <td>0.5</td>\n",
       "      <td>96</td>\n",
       "      <td>...</td>\n",
       "      <td>20</td>\n",
       "      <td>295</td>\n",
       "      <td>1752</td>\n",
       "      <td>3893</td>\n",
       "      <td>10</td>\n",
       "      <td>0</td>\n",
       "      <td>7</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>1434</td>\n",
       "      <td>0</td>\n",
       "      <td>1.4</td>\n",
       "      <td>0</td>\n",
       "      <td>11</td>\n",
       "      <td>1</td>\n",
       "      <td>49</td>\n",
       "      <td>0.5</td>\n",
       "      <td>108</td>\n",
       "      <td>...</td>\n",
       "      <td>18</td>\n",
       "      <td>749</td>\n",
       "      <td>810</td>\n",
       "      <td>1773</td>\n",
       "      <td>15</td>\n",
       "      <td>8</td>\n",
       "      <td>7</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>995</th>\n",
       "      <td>996</td>\n",
       "      <td>1700</td>\n",
       "      <td>1</td>\n",
       "      <td>1.9</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>54</td>\n",
       "      <td>0.5</td>\n",
       "      <td>170</td>\n",
       "      <td>...</td>\n",
       "      <td>17</td>\n",
       "      <td>644</td>\n",
       "      <td>913</td>\n",
       "      <td>2121</td>\n",
       "      <td>14</td>\n",
       "      <td>8</td>\n",
       "      <td>15</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>996</th>\n",
       "      <td>997</td>\n",
       "      <td>609</td>\n",
       "      <td>0</td>\n",
       "      <td>1.8</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>13</td>\n",
       "      <td>0.9</td>\n",
       "      <td>186</td>\n",
       "      <td>...</td>\n",
       "      <td>2</td>\n",
       "      <td>1152</td>\n",
       "      <td>1632</td>\n",
       "      <td>1933</td>\n",
       "      <td>8</td>\n",
       "      <td>1</td>\n",
       "      <td>19</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>997</th>\n",
       "      <td>998</td>\n",
       "      <td>1185</td>\n",
       "      <td>0</td>\n",
       "      <td>1.4</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>8</td>\n",
       "      <td>0.5</td>\n",
       "      <td>80</td>\n",
       "      <td>...</td>\n",
       "      <td>12</td>\n",
       "      <td>477</td>\n",
       "      <td>825</td>\n",
       "      <td>1223</td>\n",
       "      <td>5</td>\n",
       "      <td>0</td>\n",
       "      <td>14</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>998</th>\n",
       "      <td>999</td>\n",
       "      <td>1533</td>\n",
       "      <td>1</td>\n",
       "      <td>0.5</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>50</td>\n",
       "      <td>0.4</td>\n",
       "      <td>171</td>\n",
       "      <td>...</td>\n",
       "      <td>12</td>\n",
       "      <td>38</td>\n",
       "      <td>832</td>\n",
       "      <td>2509</td>\n",
       "      <td>15</td>\n",
       "      <td>11</td>\n",
       "      <td>6</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>999</th>\n",
       "      <td>1000</td>\n",
       "      <td>1270</td>\n",
       "      <td>1</td>\n",
       "      <td>0.5</td>\n",
       "      <td>0</td>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "      <td>35</td>\n",
       "      <td>0.1</td>\n",
       "      <td>140</td>\n",
       "      <td>...</td>\n",
       "      <td>19</td>\n",
       "      <td>457</td>\n",
       "      <td>608</td>\n",
       "      <td>2828</td>\n",
       "      <td>9</td>\n",
       "      <td>2</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>1000 rows × 21 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "       id  battery_power  blue  clock_speed  dual_sim  fc  four_g  int_memory  \\\n",
       "0       1           1043     1          1.8         1  14       0           5   \n",
       "1       2            841     1          0.5         1   4       1          61   \n",
       "2       3           1807     1          2.8         0   1       0          27   \n",
       "3       4           1546     0          0.5         1  18       1          25   \n",
       "4       5           1434     0          1.4         0  11       1          49   \n",
       "..    ...            ...   ...          ...       ...  ..     ...         ...   \n",
       "995   996           1700     1          1.9         0   0       1          54   \n",
       "996   997            609     0          1.8         1   0       0          13   \n",
       "997   998           1185     0          1.4         0   1       1           8   \n",
       "998   999           1533     1          0.5         1   0       0          50   \n",
       "999  1000           1270     1          0.5         0   4       1          35   \n",
       "\n",
       "     m_dep  mobile_wt  ...  pc  px_height  px_width   ram  sc_h  sc_w  \\\n",
       "0      0.1        193  ...  16        226      1412  3476    12     7   \n",
       "1      0.8        191  ...  12        746       857  3895     6     0   \n",
       "2      0.9        186  ...   4       1270      1366  2396    17    10   \n",
       "3      0.5         96  ...  20        295      1752  3893    10     0   \n",
       "4      0.5        108  ...  18        749       810  1773    15     8   \n",
       "..     ...        ...  ...  ..        ...       ...   ...   ...   ...   \n",
       "995    0.5        170  ...  17        644       913  2121    14     8   \n",
       "996    0.9        186  ...   2       1152      1632  1933     8     1   \n",
       "997    0.5         80  ...  12        477       825  1223     5     0   \n",
       "998    0.4        171  ...  12         38       832  2509    15    11   \n",
       "999    0.1        140  ...  19        457       608  2828     9     2   \n",
       "\n",
       "     talk_time  three_g  touch_screen  wifi  \n",
       "0            2        0             1     0  \n",
       "1            7        1             0     0  \n",
       "2           10        0             1     1  \n",
       "3            7        1             1     0  \n",
       "4            7        1             0     1  \n",
       "..         ...      ...           ...   ...  \n",
       "995         15        1             1     0  \n",
       "996         19        0             1     1  \n",
       "997         14        1             0     0  \n",
       "998          6        0             1     0  \n",
       "999          3        1             0     1  \n",
       "\n",
       "[1000 rows x 21 columns]"
      ]
     },
     "execution_count": 110,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_test"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 111,
   "metadata": {},
   "outputs": [],
   "source": [
    "X_test=df_test.drop('id',axis=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 126,
   "metadata": {},
   "outputs": [],
   "source": [
    "X_test = sc.fit_transform(X_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 162,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([3, 3, 2, 3, 1, 3, 3, 1, 3, 0, 3, 3, 0, 0, 2, 0, 2, 1, 3, 2, 1, 3,\n",
       "       1, 1, 3, 0, 2, 0, 3, 0, 2, 0, 3, 0, 1, 1, 3, 1, 2, 1, 1, 2, 0, 0,\n",
       "       0, 1, 0, 3, 1, 2, 1, 0, 3, 0, 3, 1, 3, 1, 1, 3, 3, 3, 0, 1, 0, 1,\n",
       "       2, 3, 1, 2, 1, 2, 2, 3, 3, 0, 2, 0, 1, 3, 0, 3, 3, 0, 3, 0, 3, 1,\n",
       "       3, 0, 1, 1, 2, 1, 2, 2, 0, 2, 1, 2, 1, 0, 0, 3, 0, 2, 0, 1, 2, 3,\n",
       "       3, 3, 1, 3, 3, 3, 3, 2, 3, 0, 0, 3, 2, 1, 2, 0, 3, 2, 2, 2, 0, 2,\n",
       "       2, 1, 3, 1, 1, 0, 3, 2, 1, 2, 1, 3, 2, 3, 3, 3, 2, 3, 2, 3, 1, 0,\n",
       "       3, 2, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 1, 0, 3, 0, 0, 0, 2, 1, 0, 1,\n",
       "       0, 0, 1, 2, 1, 0, 0, 1, 1, 2, 2, 1, 0, 0, 0, 1, 0, 3, 1, 0, 2, 2,\n",
       "       2, 3, 1, 2, 2, 2, 3, 2, 2, 1, 1, 0, 1, 2, 0, 2, 2, 3, 0, 2, 0, 3,\n",
       "       2, 3, 3, 1, 0, 1, 0, 3, 0, 1, 0, 2, 2, 1, 3, 1, 2, 0, 3, 1, 2, 0,\n",
       "       0, 2, 1, 3, 3, 3, 1, 1, 3, 0, 0, 2, 3, 3, 1, 3, 1, 1, 3, 2, 1, 2,\n",
       "       3, 3, 3, 1, 0, 0, 2, 3, 1, 1, 3, 2, 0, 3, 0, 0, 2, 1, 0, 3, 2, 3,\n",
       "       3, 2, 1, 3, 3, 2, 3, 1, 2, 1, 2, 0, 2, 3, 1, 0, 0, 3, 0, 3, 0, 1,\n",
       "       2, 0, 2, 3, 1, 3, 2, 2, 1, 2, 0, 0, 0, 1, 3, 2, 0, 0, 0, 3, 2, 0,\n",
       "       2, 3, 1, 2, 2, 2, 3, 1, 3, 3, 2, 2, 2, 3, 3, 0, 3, 0, 3, 1, 3, 1,\n",
       "       2, 3, 0, 1, 0, 3, 1, 3, 2, 3, 0, 0, 0, 0, 2, 0, 0, 2, 2, 1, 2, 2,\n",
       "       2, 0, 1, 0, 0, 3, 2, 0, 3, 1, 2, 2, 1, 2, 3, 1, 1, 2, 2, 1, 2, 0,\n",
       "       1, 1, 0, 3, 2, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 2, 2, 3, 2, 3, 0, 3,\n",
       "       0, 3, 0, 1, 1, 0, 2, 0, 3, 2, 3, 3, 1, 3, 1, 3, 1, 2, 2, 0, 1, 2,\n",
       "       1, 1, 0, 0, 0, 1, 2, 1, 0, 3, 2, 0, 2, 2, 0, 0, 3, 1, 2, 0, 2, 3,\n",
       "       3, 0, 3, 0, 2, 3, 2, 3, 0, 2, 0, 2, 2, 0, 1, 1, 0, 0, 1, 1, 1, 3,\n",
       "       3, 3, 2, 3, 1, 2, 2, 3, 3, 3, 2, 0, 2, 1, 2, 2, 1, 0, 2, 2, 0, 0,\n",
       "       0, 3, 1, 0, 2, 2, 2, 0, 3, 1, 2, 2, 1, 3, 0, 2, 3, 0, 1, 1, 3, 3,\n",
       "       2, 1, 1, 3, 2, 0, 3, 0, 2, 0, 3, 3, 1, 3, 2, 2, 3, 0, 1, 2, 3, 1,\n",
       "       3, 2, 3, 1, 1, 0, 0, 3, 1, 0, 3, 2, 3, 2, 0, 2, 3, 3, 2, 3, 3, 1,\n",
       "       2, 0, 2, 2, 3, 1, 0, 1, 1, 2, 2, 2, 0, 0, 2, 2, 3, 2, 0, 2, 1, 3,\n",
       "       3, 0, 1, 3, 0, 2, 1, 1, 0, 0, 2, 1, 0, 1, 1, 2, 2, 0, 2, 2, 1, 0,\n",
       "       3, 0, 0, 3, 2, 0, 0, 1, 0, 0, 3, 0, 3, 1, 3, 1, 1, 3, 2, 0, 1, 0,\n",
       "       3, 2, 2, 2, 0, 3, 0, 2, 0, 2, 0, 0, 1, 1, 1, 2, 1, 3, 1, 3, 2, 2,\n",
       "       1, 3, 2, 0, 2, 2, 0, 3, 3, 0, 2, 1, 1, 2, 0, 3, 2, 0, 3, 2, 3, 0,\n",
       "       0, 3, 0, 2, 2, 3, 2, 2, 2, 2, 1, 2, 3, 0, 1, 0, 1, 2, 1, 0, 0, 1,\n",
       "       0, 0, 3, 0, 1, 2, 0, 1, 0, 1, 3, 0, 3, 2, 3, 0, 0, 1, 2, 2, 1, 0,\n",
       "       1, 1, 0, 1, 1, 0, 0, 3, 3, 0, 3, 1, 1, 3, 0, 1, 0, 2, 1, 0, 3, 1,\n",
       "       0, 3, 1, 1, 0, 3, 3, 3, 2, 3, 0, 3, 2, 0, 0, 0, 3, 3, 2, 0, 2, 1,\n",
       "       3, 0, 0, 2, 2, 0, 3, 1, 2, 1, 1, 1, 3, 1, 1, 1, 2, 1, 0, 2, 2, 0,\n",
       "       2, 0, 0, 0, 0, 2, 3, 3, 3, 0, 1, 2, 1, 1, 0, 0, 2, 1, 0, 2, 0, 3,\n",
       "       2, 2, 1, 2, 0, 2, 1, 3, 0, 0, 3, 2, 3, 0, 0, 2, 3, 3, 1, 3, 2, 1,\n",
       "       0, 0, 3, 3, 1, 3, 0, 0, 0, 2, 2, 1, 2, 0, 3, 2, 1, 2, 3, 3, 0, 1,\n",
       "       1, 2, 1, 2, 2, 0, 1, 3, 1, 1, 3, 0, 2, 3, 2, 1, 1, 1, 3, 3, 0, 2,\n",
       "       3, 0, 2, 3, 2, 2, 2, 3, 2, 0, 1, 2, 1, 2, 1, 1, 2, 2, 2, 1, 2, 1,\n",
       "       0, 1, 3, 1, 0, 1, 2, 3, 1, 0, 0, 3, 2, 2, 3, 0, 3, 2, 2, 1, 3, 0,\n",
       "       1, 3, 1, 1, 1, 2, 3, 2, 0, 3, 0, 2, 3, 0, 3, 1, 3, 3, 1, 0, 2, 3,\n",
       "       1, 0, 2, 1, 2, 1, 2, 0, 2, 2, 0, 2, 3, 2, 3, 0, 2, 1, 1, 2, 2, 3,\n",
       "       3, 0, 2, 1, 2, 1, 3, 1, 0, 3, 0, 1, 0, 0, 3, 3, 2, 0, 0, 0, 0, 3,\n",
       "       2, 3, 3, 0, 0, 2, 1, 0, 2, 2], dtype=int64)"
      ]
     },
     "execution_count": 162,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "model = LogisticRegression()\n",
    "model.fit(x_train,y_train)\n",
    "pred=model.predict(X_test)\n",
    "pred"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
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
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}

# Проект 4. Перенос стиля на мобильном устройстве

## Оглавление  
[1. Цель](https://github.com/Victover/ds_projects/edit/main/CV_Project_4_Style%20transfer/readme.md#Цель-проекта)  
[2. Этапы выполнения проекта](https://github.com/Victover/ds_projects/edit/main/CV_Project_4_Style%20transfer/readme.md#Этапы-выполнения-проекта)  


### Цель проекта    
Основная цель проекта - создание прототипа работающей модели переноса стиля для мобильного приложения

:arrow_up:[к оглавлению](_)


### Этапы выполнения проекта    
Проект состоит из двух больших модулей. Первый - обучение модели переноса стиля с помощью Magenta, сторой - создание прототипа мобильного приложения с помощью TensorFlow Lite

**Обучение модели с помощью Magenta:**  
Обучение проводилось локально. Для установки Magenta понадобилось предварительно установить Ubuntu и Microconda3. В качестве контентных изображений были использован фрагмент ImageNet, загруженный сразу в виде TFRecord с помощью [ноутбука](https://github.com/DKudryavtsev/Skillfactory-CV/blob/master/CV_Project4-StyleTransfer/ImageNet_Download.ipynb).
Из-за отсутствия GPU и дефицита времени обучение модели проводилось не "на результат", а формально - в течение нескольких часов и с использованием только  одного субсета данных в качестве изображений стиля (dtd/images/cobwebbed)
Папка с обучением представлена в виде [скриншота](https://github.com/Victover/ds_projects/blob/main/CV_Project_4_Style%20transfer/%D0%BF%D0%B0%D0%BF%D0%BA%D0%B0%20%D1%81%20%D0%BE%D0%B1%D1%83%D1%87%D0%B5%D0%BD%D0%B8%D0%B5%D0%BC.JPG), результат инференса самодельной модели можно видеть [здесь](https://github.com/Victover/ds_projects/blob/main/CV_Project_4_Style%20transfer/inference_my%20model.JPG). Ожидаемо, он значительно хуже результата модели, полноценно обученной на полных стилевых и контентных датасетах(см. [здесь](https://github.com/Victover/ds_projects/blob/main/CV_Project_4_Style%20transfer/inference_pretrained_model.JPG) ).  
 
**Создание прототипа мобильного приложения с помощью TensorFlow Lite** 
Прототип мобильного приложения создавался с использованием готовой модели. Для этого понадобилось установить Android Studio 1.1.15. Тестирование модели проводилось с помощью эмулятора. Результат работы прототипа мобильного приложения показан [здесь](https://drive.google.com/file/d/1Wq-fgEcr8kwZtAMuj94Vxy9EYv_otSWo/view?usp=sharing). Папка с приложением представлена в виде [скриншота](https://github.com/Victover/ds_projects/blob/main/CV_Project_4_Style%20transfer/%D0%BF%D0%B0%D0%BF%D0%BA%D0%B0%20%D1%81%20%D0%BF%D1%80%D0%B8%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5%D0%BC.JPG).

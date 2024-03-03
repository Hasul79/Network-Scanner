# Network-Scanner

<div>
<img src="https://github.com/Hasul79/Network-Scanner/assets/95657084/c78e1786-6800-4eb6-982a-ca348b59a4f3">
</div>

<h1>Этот скрипт на Python представляет собой простой порт-сканер с определением служб по их баннерам. </h1>
<br>
<ol>
<li>Импорт библиотек:</li>


![Screenshot 2024-03-03 203535](https://github.com/Hasul79/Network-Scanner/assets/95657084/ad11ccc0-42fe-4fe0-8722-fccbd7da4d2e)

<br/>

<p>Здесь импортируются модули socket и sys, которые будут использоваться для работы с сокетами и обработки аргументов командной строки.</p>
 <br/>
<li>Получение IP-адреса из аргументов командной строки:</li>

![Screenshot 2024-03-03 203745](https://github.com/Hasul79/Network-Scanner/assets/95657084/00402dca-15e1-4e9a-b7b0-c285f2cf6b52)

<br/>

<p>Программа принимает IP-адрес в качестве аргумента командной строки при запуске.</p>

<br/>

<li>Словарь с общими баннерами:</li>


![Screenshot 2024-03-03 203928](https://github.com/Hasul79/Network-Scanner/assets/95657084/b5187d10-7d37-490c-8369-2c4cf32a5df2)

<br>

<p>Словарь, который содержит общие баннеры для известных служб.</p>
<br>

<li>Функция get_banner:</li>

<br/>

![Screenshot 2024-03-03 204116](https://github.com/Hasul79/Network-Scanner/assets/95657084/95499852-e29c-4020-8efc-d660a85372d9)

  <br/>
<p>Функция устанавливает соединение с заданным портом на указанном IP-адресе и получает баннер службы. Если произошла ошибка сокета, возвращается пустой байтовый объект.</p>

<br/>

<li>Функция identify_service:</li>

<br/>


![Screenshot 2024-03-03 204312](https://github.com/Hasul79/Network-Scanner/assets/95657084/c44a3754-1294-460e-a331-2922686733f2)

<br/>

<p>Функция пытается идентифицировать службу по её баннеру. В данном случае, проверяются особые условия для HTTP и HTTPS. Если баннер соответствует одному из общих баннеров, возвращается соответствующая служба, иначе возвращается None.</p>

<br/>

<li>Цикл для сканирования портов:</li>
<br/>


![Screenshot 2024-03-03 204441](https://github.com/Hasul79/Network-Scanner/assets/95657084/62907b1a-2706-41da-ac67-6f9e57082d83)

<br/>

<p>Программа проходит через цикл, в котором каждый порт от 0 до 65534 сканируется с использованием функций get_banner и identify_service. </p>

</ol>

# Если служба успешно идентифицирована, выводится сообщение о том, что порт открыт, и указывается служба.

![Screenshot 2024-03-01 152611](https://github.com/Hasul79/Network-Scanner/assets/95657084/c9de37ee-9a58-46b8-bf65-dc21af98cd73)




![Screenshot 2024-03-01 152525](https://github.com/Hasul79/Network-Scanner/assets/95657084/5dd77b22-dc09-432d-beab-4c3387197535)
![Screenshot 2024-03-01 152312](https://github.com/Hasul79/Network-Scanner/assets/95657084/65527c44-19ef-467f-abef-8162e5c1afd3)

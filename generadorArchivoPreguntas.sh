#!/bin/bash
egrep -o '(<strong class="tituloGift">[^<]+</strong>|<strong>[^<]+</strong>)' cuestionario.html  | sed s/'Puntuación: [0-9].[0-9]'//g | sed s/'<strong>'//g  | sed s/'<\/strong>'//g  | sed s/'<strong class="tituloGift">'//g > examen.txt

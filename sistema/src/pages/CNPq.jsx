import styled from 'styled-components'
import { useNavigate } from 'react-router-dom'
import { useState } from 'react'
import Topo from './comps/Topo.jsx'
import teste from './assets/teste.jpg'

export default function PesqLaboratorio(){
    const yellowcolorUTFPR = 'rgb(250, 200, 0, 0.9)';
    const [busca, setBusca] = useState('');
    const [result, setResult] = useState(['oi']);
    const Screen = styled.div`
        box-sizing: border-box;
        width: 100vw;
        height: 100vh;
        display: flex;
        flex-direction: column;
        align-items: center;
        padding: 50px 0px 0px;
    `
    const Pesquisa = styled.div`
        box-sizing: border-box;
        display: flex;
        flex-direction: column;
        align-items: center;
        width: auto;
        height: auto;
        input{
            box-sizing: border-box;
            margin: 0px 0px 5px;
            border-radius: 5px;
            border: 1px solid rgb(0, 0, 0);
            width: 200px;
            padding: 5px;
        }
    `
    const Resultados = styled.div`
        box-sizing: border-box;
        width: 50%;
        height: auto;
        display: flex;
        flex-direction: row;
        jusitfy-content: space-between;
        align-items: center;
        flex-wrap: wrap;
        margin: 20px 0px 0px;
    `
    function cnpqcar(){
        //pares = []
        //tr_lines = []
        //trf_lines = []
        //fil = open("C:/Users/DIREPQ/Desktop/cnpq.txt", 'r')
        //conj = fil.read()
        //# Divisão dos <tr e </tr
        //for i in range(0, len(conj) - 2):
        //try:
        //  if str(conj[i] + conj[i + 1] + conj[i + 2]) == '<tr':
        //      tr_lines.append(i)
        //  elif str(conj[i] + conj[i + 1] + conj[i + 2] + conj[i + 3]) == '</tr':
        //     trf_lines.append(i)
        //except IndexError:
        //   pass
        // # Trabalha no espaçõ entre o <tr e </tr
        //for a in range(0, len(tr_lines)):
        //  comeco_line = tr_lines[a]
        //  fim_line = trf_lines[a]
        //  dados = []
        //  # Analisa o intervalo
        //  for b in range(comeco_line, fim_line + 1):
        //   try:
        //    if str(conj[b] + conj[b + 1] + conj[b + 2] + conj[b + 3] + conj[b + 4]) == 'title':
        //     # Pega o nome se encontrou Title
        //     comeco_nome = 0
        //     fim_nome = 0
        //     nome = ""
        //     for c in range(b, fim_line):
        //      if comeco_nome == 0:
        //       if conj[c] == '"':
        //        comeco_nome = c + 1
        //      elif comeco_nome != 0 and fim_nome == 0:
        //       if conj[c] == '"':
        //        fim_nome = c
        //        break
        //     for d in range(comeco_nome, fim_nome):
        //      nome = nome + conj[d]
        //     nome = nome.replace('Ã§', 'ç').replace('Ã£', 'ã').replace('Ã¡', 'á').replace('Ã', 'í').replace('í©', 'é').replace('í¡', 'á').replace('í£', 'ã').replace('í´', 'ô').replace('íª', 'ê').replace('í³', 'ó').replace('í¢', 'â').replace('íº', 'ú')
        //     nome = nome.replace('ç', 'c').replace('í', 'i').replace('é', 'e').replace('á', 'a').replace('ã', 'a').replace('ô', 'o').replace('ê', 'e').replace('ó', 'o').replace('â', 'a').replace('ú', 'u')
        //     dados.append(nome)
        //   except IndexError:
        //    pass
        //  if len(dados) == 3:
        //   try:
        //    pares.index(dados)
        //   except ValueError:
        //    pares.append(dados)
        //  else:
        //   # Pegar o nome na segunda <td
        //   found = 0
        //   for b in range(comeco_line, fim_line + 1):
        //    try:
        //     if str(conj[b] + conj[b + 1] + conj[b + 2]) == '<td':
        //      found = found + 1
        //     if found == 2:
        //       comeco_linetd = b
        //       for c in range(b, fim_line):
        //         if str(conj[c] + conj[c + 1] + conj[c + 2] + conj[c + 3]) == '</td':
        //          fim_linetd = c
        //       comeconome = 0
        //       fimnome = 0
        //       for d in range(comeco_linetd + 2, fim_linetd):
        //        if conj[d] == '>' and comeconome == 0:
        //         comeconome = d
        //        elif conj[d] == '<' and fimnome == 0:
        //         fimnome = d
        //       name = ""
        //       for e in range(comeconome + 1, fimnome):
        //        name = name + conj[e]
        //      dado2 = dados[1]
        //      name = name.replace('Ã§', 'ç').replace('Ã£', 'ã').replace('Ã¡', 'á').replace('Ã', 'í').replace('í©', 'é').replace('í¡', 'á').replace('í£', 'ã').replace('í´', 'ô').replace('íª', 'ê').replace('í³', 'ó').replace('í¢', 'â').replace('íº', 'ú')
        //     name = name.replace('ç', 'c').replace('í', 'i').replace('é', 'e').replace('á', 'a').replace('ã', 'a').replace('ô', 'o').replace('ê', 'e').replace('ó', 'o').replace('â', 'a').replace('ú', 'u')
        //      dados[1] = name
        //       dados.append(dado2)
        //       pares.append(dados)
        //    except IndexError:
        //     pass
        // fil.close()
    }
    return(
        <Screen>
            <Topo/>
            <Pesquisa>
                <input placeholder=''></input>   
                <button onClick={cnpqcar}>oii</button>
            </Pesquisa>
            <Resultados>
                {result}
            </Resultados>
        </Screen>
    )
}
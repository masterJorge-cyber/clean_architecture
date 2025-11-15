## 🏴‍☠️ SOLIDify: O Tesouro da Arquitetura Limpa (Python)

-----

## 🌊 Visão Geral do Projeto

E aí, galera da Grand Line\! 🙋‍♂️

Este projeto é a nossa jornada em busca do **One Piece da Arquitetura de Software**: um código robusto, flexível e fácil de manter. Usaremos o Python, nossa Jolly Roger, para implementar os cinco princípios do **SOLID**, garantindo que nossas classes sejam tão fortes e adaptáveis quanto a tripulação do Chapéu de Palha.

Nossa meta não é apenas fazer o código funcionar, mas sim fazê-lo funcionar **direito**. Se o seu código está difícil de mudar, lento para evoluir, e cheio de acoplamentos que te fazem sentir preso em Impel Down, então este é o guia que você precisava\!

-----

## ⚓ Os Cinco Princípios do SOLID

Cada princípio SOLID nos ajuda a combater um "Almirante" da má codificação (rigidez, fragilidade, imobilidade).

| Letra | Princípio (Português) | O Que Significa | Analogia One Piece |
| :---: | :--- | :--- | :--- |
| **S** | **Single Responsibility Principle** | Uma classe deve ter apenas uma razão para mudar. | O **Zoro** deve focar em ser o melhor espadachim. Ele não deve fazer a comida nem navegar o navio. |
| **O** | **Open/Closed Principle** | Aberto para **extensão**, fechado para **modificação**. | Se o **Luffy** ganha um novo *Gear*, ele usa uma técnica nova (extensão), mas as regras básicas do seu corpo (código existente) não mudam. |
| **L** | **Liskov Substitution Principle** | Subtipos devem ser substituíveis por seus tipos base sem alterar a corretude do programa. | Um novo membro da tripulação (subtipo) deve conseguir fazer a função que lhe foi designada (tipo base) sem quebrar o barco. |
| **I** | **Interface Segregation Principle** | Clientes não devem ser forçados a depender de interfaces que não usam. | O **Usopp** só precisa da interface de *Sniper*. Ele não precisa de uma interface gigante que inclua métodos de *Navegação* e *Culinária*. |
| **D** | **Dependency Inversion Principle** | Dependa de **abstrações**, não de **detalhes** (classes concretas). | O **Capitão** (Módulo Alto Nível) dá ordens usando o título (**Navegador** - Abstração), não o nome da pessoa (**Nami** - Detalhe). Se o Navegador mudar, as ordens do Capitão não mudam. |

-----

## 🐍 Estrutura do Projeto (Python)

Neste projeto, você encontrará módulos focados em exemplos práticos de cada princípio, geralmente utilizando interfaces (classes abstratas) e Injeção de Dependência.

```
.
├── src/
│   ├── s_responsability.py     # Exemplo S: separando lógica de negócio e persistência.
│   ├── o_open_closed.py        # Exemplo O: usando classes abstratas para filtros.
│   ├── l_liskov.py             # Exemplo L: cuidado com a herança para preservar o contrato.
│   ├── i_interface_seg.py      # Exemplo I: interfaces finas e específicas.
│   └── d_dependency_inv.py     # Exemplo D: Inversão de Controle com Factories e Services.
├── interfaces/                 # Interfaces/Abstrações separadas
│   ├── base_interfaces.py      # Interfaces usadas para DIP e ISP.
├── tests/                      # Nossos testes (nunca podemos zarpar sem eles!)
└── main.py                     # O ponto de partida para ver tudo em ação.
```

-----

## 🚀 Como Executar

Para ver a arquitetura SOLID em ação, siga estes passos simples de um verdadeiro pirata:

1.  **Clone o Repositório:**

    ```bash
    git clone https://www.youtube.com/watch?v=m_6f3r-fwsE
    cd solidify-one-piece
    ```

2.  **Crie o Ambiente Virtual (Recomendado):**

    ```bash
    python -m venv .venv
    source .venv/bin/activate  # No Linux/macOS
    .\.venv\Scripts\activate   # No Windows
    ```

3.  **Instale as Dependências:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Execute o Código Principal:**

    ```bash
    python main.py
    ```

-----

## 🤝 Contribuições

Se você avistar uma ilha com um tesouro de código melhor (um novo exemplo de SOLID, refatoração, ou um teste mais rigoroso), não hesite\! **Bugs e melhorias são como frutas do diabo: difíceis de encontrar, mas essenciais para o poder\!**

1.  Faça um `fork` do projeto.
2.  Crie sua `branch` de recurso (`git checkout -b feature/minha-melhoria`).
3.  Faça suas mudanças e garanta que os testes passem.
4.  Faça o `commit` das suas mudanças.
5.  Envie um Pull Request\!

-----

## 📜 Licença

Este projeto está sob a Licença MIT. Sinta-se à vontade para usá-lo como quiser\!

**Que os ventos da arquitetura limpa soprem a nosso favor\!** 💨

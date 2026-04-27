Aqui tens o README completo e atualizado para o BioSync Nexus. Copia o conteúdo do bloco abaixo e cola diretamente no teu ficheiro README.md.

Markdown
# ⚡ BioSync Nexus

<p align="center">
  <img src="https://img.shields.io/badge/STATUS-OPERACIONAL-brightgreen?style=for-the-badge" alt="Status">
  <img src="https://img.shields.io/badge/SECURITY-LEVEL_4-red?style=for-the-badge" alt="Security">
  <img src="https://img.shields.io/badge/ENVIRONMENT-TERMINAL-black?style=for-the-badge" alt="Environment">
</p>

> **BioSync Nexus** é um sistema de gerenciamento de bio-perfis operado via CLI, projetado para oferecer imersão visual, segurança de dados e organização modular de alta performance.

---

## 🛠️ Núcleo de Processamento (Core Engine)

O sistema não se limita a armazenar dados; ele processa identidades com integridade total:
* **Gestão de Perfis:** Registro dinâmico com metadados de autoridade (Civil, Técnico, Agente, Mestre).
* **Validação Rígida:** Regras de negócio que garantem a integridade dos dados antes da persistência.
* **Arquitetura Modular:** Separação clara entre lógica (`core/`), visual (`ui/`) e persistência (`database/`).

## 🖥️ Interface Tática (Tactical UI)

Esqueça terminais monótonos. O BioSync Nexus entrega uma experiência imersiva:
* **Dashboard ANSI:** Feedback em cores para alertas críticos, sucessos e categorização de setores.
* **Arte ASCII:** Menus estilizados que transformam o terminal em uma estação de comando real.
* **UX de Campo:** Respostas instantâneas e fluxos de navegação otimizados para operadores.

## 🔍 Scanner e Monitoramento

* **Varredura Avançada:** Filtros inteligentes por Nível de Autoridade ou busca nominal instantânea.
* **Audit Log:** Rastreabilidade total. Todas as ações são registradas em `nexus_audit.log`, gerando um histórico de auditoria para segurança.

## 🛡️ Persistência e Segurança

A integridade da informação é a nossa prioridade:
* **Database JSON:** Armazenamento leve, rápido e estruturado.
* **Shadow Copy (Backup):** Sistema de espelhamento automático. A cada alteração, um `pessoas_backup.json` é gerado, prevenindo perda de dados por corrupção de arquivos.

---

## 🏗️ Estrutura do Sistema

BIOSYNC-NEXUS/
├── main.py              # O Cérebro: Orquestrador do sistema.
├── core/                # O Coração: Lógica de processamento e validação.
├── ui/                  # Os Olhos: Engine de renderização visual e cores.
└── database/            # O Cofre: Onde os bio-perfis e logs residem.

🚀 Operação
Requisitos: Certifique-se de ter o Python 3.x instalado.

Inicialização:
python main.py

Protocolo: Siga as instruções em tela para gerenciar os bio-perfis.

## 👨‍💻 Desenvolvido por

<table border="0">
  <tr>
    <td align="center">
      <a href="https://github.com/NathnF0">
        <img src="https://github.com/NathnF0.png" width="100px;" style="border-radius: 50%;" alt="Nathan Ferreira"/><br />
        <sub><b>Nathan Ferreira</b></sub>
      </a>
    </td>
    <td>
       "Sincronizando identidades através da arquitetura de software de alta fidelidade."
       <br /><br />
       <a href="https://github.com/NathnF0">
         <img src="https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white" alt="GitHub" />
       </a>
       <a href="https://www.linkedin.com/in/nathan-ferreira01">
         <img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white" alt="LinkedIn" />
       </a>
    </td>
  </tr>
</table>

---

<p align="center">
  <i>BioSync Nexus — 2026</i>
</p>

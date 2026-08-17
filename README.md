![GIRUS](girus-logo.png)

**Escolha seu idioma / Elija su idioma:** [Português](README.md) | [Español](README.es.md)

# GIRUS: Plataforma de Laboratórios Interativos

Versão 0.5.0 Codename: "Maracatu" - Maio de 2025

## Visão Geral

GIRUS é uma plataforma open-source de laboratórios interativos que permite a criação, gerenciamento e execução de ambientes de aprendizado prático para tecnologias como Linux, Docker, Kubernetes, Terraform e outras ferramentas essenciais para profissionais de DevOps, SRE, Dev e Platform Engineering.

Desenvolvida pela LINUXtips, a plataforma GIRUS se diferencia por ser executada localmente na máquina do usuário, eliminando a necessidade de infraestrutura na nuvem ou configurações complexas. Através de um CLI intuitivo, os usuários podem criar rapidamente ambientes isolados e seguros onde podem praticar e aperfeiçoar suas habilidades técnicas.

## Principais Diferenciais

- **Execução Local**: Diferentemente de outras plataformas como Katacoda ou Instruqt que funcionam como SaaS, o GIRUS é executado diretamente na máquina do usuário através de containers Docker e Kubernetes, e o melhor, é que o projeto é open source e gratuito.
- **Ambientes Isolados**: Cada laboratório é executado em um ambiente isolado no Kubernetes, garantindo segurança e evitando conflitos com o sistema host
- **Interface Intuitiva**: Terminal interativo com tarefas guiadas e validação automática de progresso
- **Fácil Instalação**: CLI simples que gerencia todo o ciclo de vida da plataforma (criação, execução e exclusão)
- **Atualização Simplificada**: Comando `update` integrado que verifica, baixa e instala novas versões automaticamente
- **Laboratórios Personalizáveis**: Sistema de templates baseado em ConfigMaps do Kubernetes que facilita a criação de novos laboratórios
- **Open Source**: Projeto totalmente aberto para contribuições da comunidade
- **Multilíngue**: Além do português, o GIRUS agora oferece suporte oficial ao espanhol. O sistema de templates permite adicionar facilmente novos idiomas.

## Trilha CKA Kubernetes

Esta versão inclui uma proposta prática de preparação para a certificação **Certified Kubernetes Administrator (CKA)**, organizada como uma trilha de **26 laboratórios Kubernetes** com filtro dedicado `CKA`.

A proposta foi desenhada para treino progressivo em ambiente local, com foco em execução prática no terminal, validação objetiva e repetição dos principais domínios cobrados em uma rotina de estudo para CKA.

### Objetivos da Trilha

Ao concluir os laboratórios CKA, a pessoa estudante deve praticar:

- criação e inspeção de Pods com `kubectl`;
- geração de YAML com `--dry-run=client -o yaml`;
- uso de namespaces, labels e selectors;
- leitura de logs, execução remota com `kubectl exec` e troubleshooting básico;
- administração de componentes do cluster e manutenção segura de nodes;
- RBAC com ServiceAccounts, Roles e RoleBindings;
- Deployments, rollouts, rollbacks, probes, requests, limits, quotas e scheduling;
- Services, Endpoints, DNS, NetworkPolicy, Ingress e descoberta de Gateway API;
- StorageClass, PersistentVolume, PersistentVolumeClaim e montagem de volumes;
- troubleshooting de Pods em falha, imagens inválidas, Services sem endpoints, PVCs pendentes e problemas de scheduling.

### Laboratórios Incluídos

| Ordem | Laboratório | Foco |
| --- | --- | --- |
| 01 | `cka-01-kubectl-pods` | Pods e comandos essenciais do `kubectl` |
| 02 | `cka-02-yaml-dry-run` | Geração de YAML com `dry-run` e aplicação declarativa |
| 03 | `cka-03-namespaces-labels-selectors` | Namespaces, labels e selectors |
| 04 | `cka-04-logs-exec-debug` | Logs, `exec` e inspeção de containers |
| 05 | `cka-05-cluster-components` | Nodes, `kube-system` e recursos da API |
| 06 | `cka-06-node-maintenance` | `cordon`, `uncordon` e manutenção segura |
| 07 | `cka-07-rbac-serviceaccounts` | RBAC e ServiceAccounts |
| 08 | `cka-08-api-helm-kustomize-crd` | API resources, CRDs e Kustomize |
| 09 | `cka-09-deployment-rollout-rollback` | Deployment, rollout e rollback |
| 10 | `cka-10-configmap-secret-env` | ConfigMaps, Secrets e variáveis de ambiente |
| 11 | `cka-11-probes-healthchecks` | Readiness e liveness probes |
| 12 | `cka-12-resources-quotas-limits` | Requests, limits e ResourceQuota |
| 13 | `cka-13-scheduling-nodeselector` | Scheduling com `nodeSelector` |
| 14 | `cka-14-jobs-cronjobs` | Jobs e CronJobs |
| 15 | `cka-15-hpa-autoscaling` | HPA e dependência de métricas |
| 16 | `cka-16-services-endpoints` | Services e Endpoints |
| 17 | `cka-17-dns-coredns` | DNS interno com CoreDNS |
| 18 | `cka-18-networkpolicy` | NetworkPolicy e isolamento de tráfego |
| 19 | `cka-19-ingress` | Ingress para Services HTTP |
| 20 | `cka-20-gateway-api-discovery` | Descoberta de Gateway API |
| 21 | `cka-21-storageclass-pvc` | StorageClass e PVC dinâmico |
| 22 | `cka-22-pv-pvc-static` | PV e PVC estático |
| 23 | `cka-23-volume-mounts` | Montagem de volumes em Pods |
| 24 | `cka-24-troubleshoot-crashloop` | Troubleshooting de falhas de containers |
| 25 | `cka-25-troubleshoot-image-service` | Imagem inválida e Service sem endpoint |
| 26 | `cka-26-troubleshoot-pending-rbac-pvc` | Pending, RBAC e PVC em conjunto |

### Modelo Pedagógico

Cada laboratório CKA possui:

- texto de fixação explicando a proposta do exercício;
- explicação dos principais comandos e parâmetros usados;
- referências para a documentação oficial do Kubernetes;
- validações automáticas para confirmar o estado esperado;
- conclusão com reforço do conhecimento aprendido;
- nome de tarefa ajustado para aparecer corretamente em **Conhecimentos adquiridos** ao finalizar o lab.

### Referências Oficiais

Os laboratórios apontam para páginas oficiais da documentação Kubernetes, incluindo:

- [`kubectl` reference](https://kubernetes.io/docs/reference/kubectl/)
- [`kubectl run`](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_run/)
- [Pods](https://kubernetes.io/docs/concepts/workloads/pods/)
- [Deployments](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)
- [Services](https://kubernetes.io/docs/concepts/services-networking/service/)
- [DNS for Services and Pods](https://kubernetes.io/docs/concepts/services-networking/dns-pod-service/)
- [Network Policies](https://kubernetes.io/docs/concepts/services-networking/network-policies/)
- [Ingress](https://kubernetes.io/docs/concepts/services-networking/ingress/)
- [Persistent Volumes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/)
- [Resource Management](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/)
- [Assigning Pods to Nodes](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/)

### Como Usar no GIRUS

Após subir a plataforma GIRUS, acesse a tela de laboratórios e use o filtro **CKA** para visualizar a trilha em ordem:

```text
CKA 01 -> CKA 02 -> ... -> CKA 26
```

Os mesmos laboratórios também aparecem no filtro **Kubernetes**, pois a trilha CKA é uma trilha prática de administração Kubernetes.

Recomendação de estudo:

1. Execute o lab consultando as instruções.
2. Repita sem copiar os comandos.
3. Quebre algo de propósito e diagnostique.
4. Refaça contra o relógio.
5. Anote qual comando provou que a solução funcionou.

## Trilha RHCSA Linux/RHEL

Esta versão também inclui uma proposta prática de preparação para a certificação **Red Hat Certified System Administrator (RHCSA)**, organizada como uma trilha de **26 laboratórios Linux/RHEL** com filtro dedicado **RHCSA**.

A trilha segue a progressão dos treinamentos oficiais Red Hat **RH124**, **RH134** e **RH200/RH199**: fundamentos de administração, administração avançada e revisão acelerada para prova prática. Como os laboratórios rodam em container local, comandos que dependem de uma instalação RHEL completa, como `systemctl`, `dnf`, SELinux ativo, particionamento real, LVM real, `firewall-cmd`, Podman ou Kickstart, são tratados com roteiro controlado e explicação clara de aplicação em RHEL real.

### Objetivos da Trilha

Ao concluir os laboratórios RHCSA, a pessoa estudante deve praticar:

- navegação no shell, documentação local e manipulação de arquivos;
- redirecionamento, pipes, filtros e expressões regulares;
- usuários, grupos, permissões, ownership e umask;
- software com RPM/DNF em contexto RHEL;
- processos, jobs, sinais, serviços e systemd;
- rede, SSH, NetworkManager e segurança de portas;
- shell scripting, cron, timers e automação básica;
- logs, journalctl, rsyslog e troubleshooting;
- SELinux, contextos, firewall e controles de acesso;
- arquivos compactados, transferência, storage, LVM, swap, NFS e autofs;
- Podman, Kickstart, Cockpit, image mode e revisão integrada RHCSA.

### Laboratórios Incluídos

| Ordem | Laboratório | Foco |
| --- | --- | --- |
| 01 | `rhcsa-01-rhel-ecosystem-cli` | Introdução ao RHEL, shell e contexto do sistema |
| 02 | `rhcsa-02-help-docs-man-pages` | Ajuda local, `man` e `--help` |
| 03 | `rhcsa-03-filesystem-navigation` | Hierarquia de filesystem e caminhos |
| 04 | `rhcsa-04-file-management-editing` | Criação, cópia, movimentação e edição de arquivos |
| 05 | `rhcsa-05-redirection-pipelines-grep` | Redirecionamento, pipes e `grep` |
| 06 | `rhcsa-06-users-groups-passwords` | Usuários, grupos e comandos reais de RHEL |
| 07 | `rhcsa-07-permissions-acl-umask` | Permissões, ownership e umask |
| 08 | `rhcsa-08-software-rpm-dnf` | RPM, DNF e repositórios |
| 09 | `rhcsa-09-processes-jobs-signals` | Processos, jobs e sinais |
| 10 | `rhcsa-10-services-systemd` | Serviços, systemd e PID 1 |
| 11 | `rhcsa-11-networking-nmcli-ip` | Rede, IP, rotas e NetworkManager |
| 12 | `rhcsa-12-ssh-remote-access` | SSH, chaves e acesso remoto |
| 13 | `rhcsa-13-shell-scripting` | Shell scripting para administração |
| 14 | `rhcsa-14-regex-text-processing` | Regex e processamento de texto |
| 15 | `rhcsa-15-scheduling-at-cron-systemd-timers` | Cron, `at` e systemd timers |
| 16 | `rhcsa-16-logs-journalctl-rsyslog` | Logs, journalctl e rsyslog |
| 17 | `rhcsa-17-selinux-basics-contexts` | SELinux, modos e contextos |
| 18 | `rhcsa-18-archives-transfer` | `tar`, compressão e transferência |
| 19 | `rhcsa-19-storage-partitions-filesystems` | Storage básico, partições e filesystems |
| 20 | `rhcsa-20-lvm-swap-storage` | LVM, swap e crescimento de volumes |
| 21 | `rhcsa-21-boot-targets-recovery` | Boot, targets e recuperação |
| 22 | `rhcsa-22-firewall-network-security` | Firewall, portas e segurança de rede |
| 23 | `rhcsa-23-nfs-autofs` | NFS e automount |
| 24 | `rhcsa-24-podman-containers` | Containers com Podman |
| 25 | `rhcsa-25-kickstart-image-mode-cockpit` | Kickstart, Cockpit e image mode |
| 26 | `rhcsa-26-rhcsa-comprehensive-review` | Revisão integrada RHCSA |

### Modelo Pedagógico

Cada laboratório RHCSA possui:

- texto de fixação explicando a proposta, o contexto e o domínio estudado;
- explicação dos comandos, parâmetros e redirecionamentos usados;
- separação entre atalho de laboratório e comando aplicável em RHEL real;
- referências oficiais Red Hat para RH124, RH134 ou RH200/RH199;
- validação automática executável no ambiente GIRUS;
- conclusão reforçando o conhecimento aplicado no lab.

### Referências Oficiais

Os laboratórios apontam para as páginas oficiais de treinamento da Red Hat:

- [RH124 - Red Hat System Administration I](https://www.redhat.com/en/services/training/rh124-red-hat-system-administration-i)
- [RH134 - Red Hat System Administration II](https://www.redhat.com/en/services/training/rh134-red-hat-system-administration-ii)
- [RH200 - Red Hat Certified System Administrator Rapid Track course with exam](https://www.redhat.com/en/services/training/rh200-red-hat-certified-system-administrator-rapid-track-course-exam)

### Como Usar no GIRUS

Após subir a plataforma GIRUS, acesse a tela de laboratórios e use o filtro **RHCSA** para visualizar a trilha em ordem:

```text
RHCSA 01 -> RHCSA 02 -> ... -> RHCSA 26
```

Os laboratórios RHCSA também aparecem no filtro **Linux**, pois a trilha é uma trilha prática de administração Linux/RHEL. O filtro **RHCSA** usa ícone personalizado Red Hat para facilitar a identificação visual dos cards.

### Ajuste do Bundle Frontend

O frontend atualmente é servido a partir de um bundle JavaScript já compilado no pod Nginx. Quando a trilha RHCSA for aplicada em uma instalação existente, também é necessário publicar um bundle com o filtro **RHCSA**. O repositório inclui o script `scripts/patch-rhcsa-frontend-bundle.py` para reproduzir esse ajuste a partir do bundle original:

```bash
python scripts/patch-rhcsa-frontend-bundle.py main.9081a282.js main.9081a282.rhcsa.js
```

Depois copie o bundle e o ícone para o pod frontend e atualize o `index.html`:

```bash
FRONTEND_POD=$(kubectl get pod -n girus -l app=girus-frontend -o jsonpath='{.items[0].metadata.name}')

kubectl cp main.9081a282.rhcsa.js girus/${FRONTEND_POD}:/usr/share/nginx/html/static/js/main.9081a282.rhcsa.js
kubectl cp assets/images/rhcsa-redhat-icon.webp girus/${FRONTEND_POD}:/usr/share/nginx/html/assets/images/rhcsa-redhat-icon.webp

kubectl exec -n girus ${FRONTEND_POD} -- sh -c "sed -i 's/main\.[^\" ]*\.js/main.9081a282.rhcsa.js/g' /usr/share/nginx/html/index.html"
```

Validação rápida:

```bash
curl -s http://localhost:8000/static/js/main.9081a282.rhcsa.js | grep 'label:"RHCSA"'
curl -s http://localhost:8000/labs | grep 'main.9081a282.rhcsa.js'
```

## Gerenciamento de Repositórios e Laboratórios

O GIRUS implementa um sistema robusto de gerenciamento de repositórios e laboratórios, similar ao Helm para Kubernetes. Este sistema permite:

### Instalação
```bash
curl -sSL girus.linuxtips.io | bash
```

Você precisa ter o Docker instalado em seu computador para poder instalar o Girus.

### Atualização da CLI

- **Verificar e Atualizar para a Última Versão**:
  ```bash
  girus update
  ```
  Este comando verifica se há uma versão mais recente do GIRUS CLI disponível, baixa e instala a atualização, oferecendo a opção de recriar o cluster após a atualização para garantir compatibilidade.

### Repositórios

- **Adicionar Repositórios**: 
  ```bash
  girus repo add linuxtips https://github.com/linuxtips/labs/raw/main
  ```

- **Listar Repositórios**:
  ```bash
  girus repo list
  ```

- **Remover Repositórios**:
  ```bash
  girus repo remove linuxtips
  ```

- **Atualizar Repositórios**:
  ```bash
  girus repo update linuxtips https://github.com/linuxtips/labs/raw/main
  ```

### Suporte a Repositórios Locais (file://)

O GIRUS agora suporta repositórios locais usando o prefixo `file://`. Isso é útil para testar laboratórios ou desenvolver repositórios sem precisar publicar em um servidor remoto.

#### Exemplo de uso:

```bash
# Adicionando um repositório local
./girus repo add meu-local file:///caminho/absoluto/para/seu-repo

# Exemplo prático:
./girus repo add test-repo file:///home/jeferson/REPOS/teste/girus-cli/test-repo
```

> **Nota:** O caminho após `file://` deve ser absoluto e apontar para o diretório onde está o `index.yaml` do repositório.

Você pode listar, buscar e instalar laboratórios normalmente a partir de repositórios locais, assim como faria com repositórios remotos.

### Laboratórios

- **Listar Laboratórios Disponíveis**:
  ```bash
  girus lab list
  ```

- **Instalar Laboratório**:
  ```bash
  girus lab install linuxtips linux-basics
  ```

- **Buscar Laboratórios**:
  ```bash
  girus lab search docker
  ```

### Estrutura de Repositórios

Os repositórios seguem uma estrutura padronizada:

```
repositorio/
├── index.yaml           # Índice do repositório
└── labs/               # Diretório contendo os laboratórios
    ├── lab1/
    │   ├── lab.yaml    # Definição do laboratório
    │   └── assets/     # Recursos do laboratório (opcional)
    └── lab2/
        ├── lab.yaml
        └── assets/
```

### Formato dos Arquivos

#### index.yaml
```yaml
apiVersion: v1
generated: "2024-03-20T10:00:00Z"
entries:
  lab-name:
    - name: lab-name
      version: "1.0.0"
      description: "Descrição do laboratório"
      keywords:
        - keyword1
        - keyword2
      maintainers:
        - "Nome <email@exemplo.com>"
      url: "https://github.com/seu-repo/raw/main/labs/lab-name/lab.yaml"
      created: "2024-03-20T10:00:00Z"
      digest: "sha256:hash-do-arquivo"
```

#### lab.yaml
```yaml
apiVersion: girus.linuxtips.io/v1
kind: Lab
metadata:
  name: lab-name
  version: "1.0.0"
  description: "Descrição do laboratório"
  author: "Nome do Autor"
  created: "2024-03-20T10:00:00Z"
spec:
  environment:
    image: ubuntu:22.04
    resources:
      cpu: "1"
      memory: "1Gi"
    volumes:
      - name: workspace
        mountPath: /workspace
        size: "1Gi"

  tasks:
    - name: "Nome da Tarefa"
      description: "Descrição da tarefa"
      steps:
        - description: "Descrição do passo"
          command: "comando"
          expectedOutput: "saída esperada"
          hint: "Dica para o usuário"

  validation:
    - name: "Nome da Validação"
      description: "Descrição da validação"
      checks:
        - command: "comando"
          expectedOutput: "saída esperada"
          errorMessage: "Mensagem de erro"
```

## Arquitetura

O projeto GIRUS é composto por quatro componentes principais:

1. **GIRUS CLI**: Ferramenta de linha de comando que gerencia todo o ciclo de vida da plataforma
2. **Backend**: API Golang que orquestra os laboratórios através da API do Kubernetes
3. **Frontend**: Interface web React que fornece acesso ao terminal interativo e às tarefas
4. **Templates de Laboratórios**: Definições YAML para os diferentes laboratórios disponíveis

### Diagrama de Fluxo de Arquitetura

```
┌─────────────┐     ┌──────────────┐     ┌──────────────┐
│  GIRUS CLI  │────▶│ Kind Cluster │────▶│ Kubernetes   │
└─────────────┘     └──────────────┘     └──────────────┘
                                               │
                                               ▼
┌─────────────┐     ┌──────────────┐     ┌──────────────┐
│  Terminal   │◀───▶│   Frontend   │◀───▶│   Backend    │
│ Interativo  │     │    (React)   │     │     (Go)     │
└─────────────┘     └──────────────┘     └──────────────┘
                                               │
                                               ▼
                                         ┌──────────────┐
                                         │  Templates   │
                                         │     Labs     │
                                         └──────────────┘
```

## Componentes Detalhados

### GIRUS CLI

GIRUS (GIRUS Is Really Useful System) é uma ferramenta CLI desenvolvida pela LINUXtips para criar e gerenciar ambientes de laboratório práticos.

## Instalação

### Usando o script de instalação

```bash
curl -sSL girus.linuxtips.io | bash
```

### Usando o Makefile

Clone o repositório e execute `make <comando>`.

Aqui estão os comandos disponíveis:

### Compilação e Instalação

* **`make build`** (ou simplesmente `make`): Compila o binário `girus` para o seu sistema operacional atual e o coloca no diretório `dist/`. Este é o comando padrão se você executar `make` sem argumentos.
* **`make install`**: Compila o binário (se ainda não estiver compilado) e o move para `/usr/local/bin/girus`, tornando-o acessível globalmente no seu sistema. Requer permissões de superusuário (`sudo`).
* **`make clean`**: Remove o diretório `dist/` e todos os arquivos de build gerados.
* **`make release`**: Compila o binário `girus` para múltiplas plataformas (Linux, macOS, Windows - amd64 e arm64) e os coloca no diretório `dist/`.

### Versionamento

O GIRUS CLI utiliza um sistema de versionamento dinâmico baseado em git tags. O processo de build detecta automaticamente a versão com base nos seguintes critérios:

* Se existir uma tag git (ex: `v0.3.0`), essa versão será utilizada removendo o prefixo `v` (resultado: `0.3.0`)
* Se não existirem tags, será utilizada a versão padrão `0.3.0`
* Para builds locais, você pode compilar com uma versão específica através do seguinte comando:

```bash
go build -o girus -ldflags="-X 'github.com/badtuxx/girus-cli/internal/common.Version=0.5.0'" ./main.go
```

Para verificar a versão atual do binário, execute:

```bash
./girus version
```

Os workflows CI/CD do projeto também utilizam este mecanismo de versionamento dinâmico para as builds do Docker e artefatos de release, garantindo consistência em todo o processo de build.

### Gerenciamento de Dependências (Go Modules)

* **`make check-updates`**: Verifica se há atualizações disponíveis para as dependências Go do projeto.
* **`make upgrade-all`**: Atualiza todas as dependências Go para suas versões mais recentes e executa `go mod tidy`.
* **`make upgrade MODULE=<nome/do/modulo>`**: Atualiza uma dependência Go específica para a versão mais recente. Substitua `<nome/do/modulo>` pelo caminho do módulo (ex: `make upgrade MODULE=github.com/spf13/cobra`).
* **`make tidy`**: Executa `go mod tidy` para remover dependências não utilizadas e limpar os arquivos `go.mod` e `go.sum`.
* **`make deps`**: Exibe o gráfico de dependências do projeto.

### Primeiros Passos
## Criando seu Primeiro Cluster
Após instalar o GIRUS, o primeiro passo é criar um cluster Kubernetes local usando Kind:

  ```bash
  girus create cluster
  ```
## Este comando irá:

- **Verificar se o Docker está rodando**
- **Instalar o Kind (se não estiver presente)**
- **Criar um cluster Kubernetes local**
- **Instalar os componentes do GIRUS (backend, frontend, etc.)**
- **Configurar os serviços necessários**

> **Nota:** O processo pode levar alguns minutos na primeira execução, pois precisa baixar as imagens Docker necessárias.

- **Verificando o Status do Cluster**:
Para verificar se o cluster foi criado com sucesso:
  ```bash
  # Verificar clusters Kind disponíveis
  kind get clusters

  # Verificar pods do GIRUS
  kubectl get pods -n girus

  # Verificar serviços do GIRUS
  kubectl get services -n girus
  ```

**Gerenciando o Cluster**:
Para verificar o status:
  ```bash
  # Listar clusters disponíveis
  kind get clusters

  # Verificar se o cluster está saudável
  kubectl cluster-info
  ```

 **Deletar o Cluster**:

  ```bash
  # Remover o cluster quando não precisar mais
  kind delete cluster --name girus
  ```
**Recriar o Cluster**:

  ```bash
  # Se precisar recriar o cluster
  kind delete cluster --name girus
  girus create cluster
  ```

## Repositório de Labs

Este repositório contém uma coleção de labs práticos para diferentes tecnologias, organizados nas seguintes categorias:

### AWS Labs
- AWS LocalStack com Terraform
- AWS S3 Storage
- AWS DynamoDB NoSQL
- AWS Lambda Serverless

### Terraform Labs
- Fundamentos do Terraform
- Terraform com AWS
- Provisioners e Módulos no Terraform

### Kubernetes Labs
- Fundamentos do Kubernetes
- Deployment no Kubernetes
- Exploração de Recursos
- Serviços e Redes
- ConfigMaps e Secrets
- CronJobs

### Docker Labs
- Fundamentos do Docker
- Gerenciamento de Containers
- Fundamentos de Redes
- Volumes
- Docker Compose

### Linux Labs
- Comandos Básicos
- Gerenciamento de Usuários
- Permissões de Arquivos
- Processamento de Texto
- Gerenciamento de Processos
- Shell Script
- Monitoramento de Sistema

## Usando os Labs

### Adicionar o Repositório

```bash
# Adicionar o repositório oficial
girus repo add girus-cli https://raw.githubusercontent.com/badtuxx/girus-cli/main/index.yaml

# Ou adicionar localmente para desenvolvimento
girus repo add girus-cli file:///caminho/para/girus-cli
```

### Listar Labs Disponíveis

```bash
girus lab list
```

### Iniciar um Lab

```bash
girus lab start <nome-do-lab>
```

Por exemplo:
```bash
girus lab start aws_localstack_terraform
```

## Contribuindo com Labs

Para contribuir com novos labs, siga estas etapas:

1. Crie um novo diretório em `labs/<nome-do-lab>`
2. Adicione um arquivo `lab.yaml` com a estrutura do lab
3. Atualize o `index.yaml` com as informações do novo lab
4. Envie um Pull Request

### Estrutura do Lab

```yaml
name: nome-do-lab
title: "Título do Lab"
description: "Descrição detalhada do lab"
duration: 45m
image: "ubuntu:20.04"
tasks:
  - name: "Nome da Tarefa"
    description: "Descrição da tarefa"
    steps:
      - "Passo 1: Faça isso"
      - "Passo 2: Execute aquilo"
    validation:
      - command: "comando para verificar"
        expectedOutput: "saída esperada"
        errorMessage: "Mensagem de erro personalizada"
```

## Suporte e Contato

* **GitHub Issues**: [github.com/badtuxx/girus-cli/issues](https://github.com/badtuxx/girus-cli/issues)
* **GitHub Discussions**: [github.com/badtuxx/girus-cli/discussions](https://github.com/badtuxx/girus-cli/discussions)
* **Discord da Comunidade**: [discord.gg/linuxtips](https://discord.gg/linuxtips)

## Licença

Este projeto é distribuído sob a licença GPL-3.0. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## Agradecimentos

O GIRUS é possível graças à contribuição de muitas pessoas e projetos:

- **Equipe LINUXtips**: Pelo desenvolvimento e manutenção do projeto
- **Contribuidores**: Desenvolvedores, criadores de conteúdo e tradutores
- **Projetos Open Source**: Go, React, Kubernetes, Kind, Docker e muitos outros
- **Comunidade**: Todos os usuários e apoiadores que acreditam no projeto

---

## FAQ - Perguntas Frequentes

**Q: O GIRUS funciona offline?**  
A: Sim, após a instalação inicial e download das imagens, o GIRUS pode funcionar completamente offline.

**Q: Quanto consome de recursos da minha máquina?**  
A: O GIRUS é otimizado para ser leve. Um cluster básico consome aproximadamente 1-2GB de RAM e requer cerca de 5GB de espaço em disco.

**Q: Posso criar laboratórios personalizados para minha equipe/empresa?**  
A: Absolutamente! O sistema de templates é flexível e permite a criação de laboratórios específicos para suas necessidades.

**Q: Como faço para atualizar o GIRUS para a versão mais recente?**  
A: Execute o comando `girus update`. O comando verificará se há uma versão mais recente disponível e, se houver, executará a atualização automaticamente. Após a atualização, você terá a opção de recriar o cluster para garantir a compatibilidade com as novas funcionalidades.

**Q: O GIRUS funciona em ambientes corporativos com restrições de rede?**  
A: Sim, após o download inicial das imagens, o GIRUS opera localmente sem necessidade de conexão externa.

**Q: Posso contribuir com novos laboratórios para o projeto?**  
A: Definitivamente! Contribuições são bem-vindas e valorizadas. Consulte a seção ["Contribuição e Comunidade"](#contribui%C3%A7%C3%A3o-e-comunidade) para detalhes.

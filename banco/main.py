#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Módulo principal do sistema bancário.

Este módulo contém a interface de linha de comando para interação com o sistema bancário,
permitindo cadastrar usuários, realizar depósitos, saques e consultar saldo.
"""

import os
import sys
from usuario import Usuario


class SistemaBancario:
    """
    Classe que implementa a interface do sistema bancário.
    
    Esta classe gerencia a interação com o usuário através de um menu de opções,
    permitindo cadastrar usuários, realizar operações financeiras e consultar informações.
    
    Attributes
    ----------
    usuarios : dict
        Dicionário que armazena os usuários cadastrados, com o nome como chave.
    usuario_atual : Usuario or None
        Referência para o usuário atualmente selecionado.
    """
    
    def __init__(self):
        """
        Inicializa o sistema bancário com uma lista vazia de usuários.
        """
        self.usuarios = {}
        self.usuario_atual = None
    
    def limpar_tela(self):
        """
        Limpa a tela do terminal para melhorar a experiência do usuário.
        """
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def exibir_menu_principal(self):
        """
        Exibe o menu principal do sistema bancário.
        
        Returns
        -------
        int
            Opção selecionada pelo usuário.
        """
        self.limpar_tela()
        print("===== SISTEMA BANCÁRIO =====\n")
        print("1. Cadastrar Novo Usuário")
        print("2. Selecionar Usuário Existente")
        print("3. Listar Usuários Cadastrados")
        print("0. Sair")
        
        try:
            opcao = int(input("\nEscolha uma opção: "))
            return opcao
        except ValueError:
            return -1
    
    def exibir_menu_usuario(self):
        """
        Exibe o menu de operações para um usuário selecionado.
        
        Returns
        -------
        int
            Opção selecionada pelo usuário.
        """
        self.limpar_tela()
        print(f"===== USUÁRIO: {self.usuario_atual.nome} =====\n")
        print(f"Saldo Atual: R$ {self.usuario_atual.consultar_saldo():.2f}\n")
        print("1. Depositar")
        print("2. Sacar")
        print("3. Consultar Histórico")
        print("0. Voltar ao Menu Principal")
        
        try:
            opcao = int(input("\nEscolha uma opção: "))
            return opcao
        except ValueError:
            return -1
    
    def cadastrar_usuario(self):
        """
        Cadastra um novo usuário no sistema.
        """
        self.limpar_tela()
        print("===== CADASTRO DE USUÁRIO =====\n")
        
        nome = input("Nome do usuário: ")
        
        if nome in self.usuarios:
            input("\nUsuário já cadastrado. Pressione Enter para continuar...")
            return
        
        try:
            saldo_inicial = float(input("Saldo inicial: R$ "))
            if saldo_inicial < 0:
                raise ValueError("O saldo inicial não pode ser negativo.")
        except ValueError as e:
            input(f"\nValor inválido: {str(e)}. Pressione Enter para continuar...")
            return
        
        usuario = Usuario(nome, saldo_inicial)
        self.usuarios[nome] = usuario
        
        input("\nUsuário cadastrado com sucesso! Pressione Enter para continuar...")
    
    def selecionar_usuario(self):
        """
        Permite selecionar um usuário existente para realizar operações.
        
        Returns
        -------
        bool
            True se um usuário foi selecionado com sucesso, False caso contrário.
        """
        self.limpar_tela()
        print("===== SELECIONAR USUÁRIO =====\n")
        
        if not self.usuarios:
            input("Nenhum usuário cadastrado. Pressione Enter para continuar...")
            return False
        
        print("Usuários cadastrados:")
        for i, nome in enumerate(self.usuarios.keys(), 1):
            print(f"{i}. {nome}")
        
        try:
            indice = int(input("\nSelecione o número do usuário (0 para cancelar): "))
            if indice == 0:
                return False
            
            if 1 <= indice <= len(self.usuarios):
                nome = list(self.usuarios.keys())[indice - 1]
                self.usuario_atual = self.usuarios[nome]
                return True
            else:
                input("\nOpção inválida. Pressione Enter para continuar...")
                return False
        except ValueError:
            input("\nOpção inválida. Pressione Enter para continuar...")
            return False
    
    def listar_usuarios(self):
        """
        Lista todos os usuários cadastrados no sistema.
        """
        self.limpar_tela()
        print("===== USUÁRIOS CADASTRADOS =====\n")
        
        if not self.usuarios:
            print("Nenhum usuário cadastrado.")
        else:
            for nome, usuario in self.usuarios.items():
                print(f"{nome}: R$ {usuario.consultar_saldo():.2f}")
        
        input("\nPressione Enter para continuar...")
    
    def realizar_deposito(self):
        """
        Realiza um depósito na conta do usuário atual.
        """
        self.limpar_tela()
        print("===== DEPÓSITO =====\n")
        print(f"Usuário: {self.usuario_atual.nome}")
        print(f"Saldo Atual: R$ {self.usuario_atual.consultar_saldo():.2f}\n")
        
        try:
            valor = float(input("Valor do depósito: R$ "))
            self.usuario_atual.depositar(valor)
            print(f"\nDepósito de R$ {valor:.2f} realizado com sucesso!")
            print(f"Novo saldo: R$ {self.usuario_atual.consultar_saldo():.2f}")
        except ValueError as e:
            print(f"\nErro: {str(e)}")
        
        input("\nPressione Enter para continuar...")
    
    def realizar_saque(self):
        """
        Realiza um saque na conta do usuário atual.
        """
        self.limpar_tela()
        print("===== SAQUE =====\n")
        print(f"Usuário: {self.usuario_atual.nome}")
        print(f"Saldo Atual: R$ {self.usuario_atual.consultar_saldo():.2f}\n")
        
        try:
            valor = float(input("Valor do saque: R$ "))
            self.usuario_atual.sacar(valor)
            print(f"\nSaque de R$ {valor:.2f} realizado com sucesso!")
            print(f"Novo saldo: R$ {self.usuario_atual.consultar_saldo():.2f}")
        except ValueError as e:
            print(f"\nErro: {str(e)}")
        
        input("\nPressione Enter para continuar...")
    
    def consultar_historico(self):
        """
        Exibe o histórico de transações do usuário atual.
        """
        self.limpar_tela()
        print("===== HISTÓRICO DE TRANSAÇÕES =====\n")
        print(f"Usuário: {self.usuario_atual.nome}\n")
        
        historico = self.usuario_atual.obter_historico()
        
        if not historico:
            print("Nenhuma transação registrada.")
        else:
            for i, transacao in enumerate(historico, 1):
                data = transacao["data"].strftime("%d/%m/%Y %H:%M:%S")
                tipo = transacao["tipo"]
                valor = transacao["valor"]
                
                if tipo == "Saque":
                    print(f"{i}. [{data}] {tipo}: R$ {abs(valor):.2f}")
                else:
                    print(f"{i}. [{data}] {tipo}: R$ {valor:.2f}")
        
        input("\nPressione Enter para continuar...")
    
    def executar(self):
        """
        Executa o sistema bancário, exibindo menus e processando as opções escolhidas.
        """
        while True:
            opcao = self.exibir_menu_principal()
            
            if opcao == 0:
                self.limpar_tela()
                print("Obrigado por utilizar o Sistema Bancário!")
                sys.exit(0)
            elif opcao == 1:
                self.cadastrar_usuario()
            elif opcao == 2:
                if self.selecionar_usuario():
                    self.menu_usuario()
            elif opcao == 3:
                self.listar_usuarios()
            else:
                input("\nOpção inválida. Pressione Enter para continuar...")
    
    def menu_usuario(self):
        """
        Gerencia o menu de operações do usuário selecionado.
        """
        while True:
            opcao = self.exibir_menu_usuario()
            
            if opcao == 0:
                break
            elif opcao == 1:
                self.realizar_deposito()
            elif opcao == 2:
                self.realizar_saque()
            elif opcao == 3:
                self.consultar_historico()
            else:
                input("\nOpção inválida. Pressione Enter para continuar...")


if __name__ == "__main__":
    sistema = SistemaBancario()
    sistema.executar()
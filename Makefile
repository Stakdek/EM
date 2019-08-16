SHELL := /bin/bash

BUILD = install.sh

.PHONY: install
install:
	sudo bash $(BUILD)
clean:
	rm -rf *.pyc
	rm -rf *~*
stop:
	sudo systemctl stop em.service
	sudo systemctl disable em.service
start:
	sudo systemctl daemon-reload
	sudo systemctl enable em.service
	sudo systemctl restart em.service

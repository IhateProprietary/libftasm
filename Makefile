#******************************************************************************#
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jye <marvin@42.fr>                         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/04/04 14:58:08 by jye               #+#    #+#              #
#    Updated: 2019/04/04 15:21:29 by jye              ###   ########.fr        #
#                                                                              #
#******************************************************************************#

ASMC = nasm
ASMFLAGS = -fmacho64

ASMSOURCE = ft_bzero.s \
			ft_cat.s \
			ft_isalnum.s \
			ft_isalpha.s \
			ft_isascii.s \
			ft_isdigit.s \
			ft_isprint.s \
			ft_memchr.s \
			ft_memcmp.s \
			ft_memcpy.s \
			ft_memset.s \
			ft_puts.s \
			ft_strchr.s \
			ft_strcmp.s \
			ft_strdup.s \
			ft_strlen.s \
			ft_tolower.s \
			ft_toupper.s

TARGET = libfts.a

all: $(TARGET)

$(TARGET): $(addsuffix .o, $(basename $(ASMSOURCE)))
	ar -rcs $(TARGET) $^

%.o: %.s
	$(ASMC) $(ASMFLAGS) $< -o $@

clean:
	rm -rf $(addsuffix .o, $(basename $(ASMSOURCE)))

fclean: clean
	rm -rf $(TARGET)

re: fclean all

.PHONY: all fclean clean re

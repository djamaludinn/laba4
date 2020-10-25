#!/usr/bin/env python3
# -*- config: utf-8 -*-

if __name__ == '__main__':
    for i in range(1, 10):
        for j in range(0, 10):
            for k in range(0, 10):
                if i + j + k == i * j * k:
                    print(f"{i}{j}{k}")

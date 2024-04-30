# Herança

class Camera():
    def __init__(self, marca, resolucao):
        self.marca = marca
        self.resolução = resolucao

    def tirar_foto(self):
        print(f'Foto tirada com a câmera {
              self.marca} e com a resolução de {self.resolução} megapixels')


Camera1 = Camera('Sony', '16MP')
Camera1.tirar_foto()


class Camera_Celular(Camera):
    def __init__(self, marca, resolucao, celular):
        super().__init__(marca, resolucao)
        self.celular = celular

    def tirar_foto(self, camera_a_utilizar):
        print(f'Foto tirada com o celular {self.celular}, marca {self.marca} e com a resolução de {
              self.resolução} megapixels, utilizando a câmera {camera_a_utilizar}')


Camera2 = Camera_Celular('Apple', '16MP', 'Iphone 15 Pro')
Camera2.tirar_foto(2)


class Camera_Seguranca(Camera):
    def __init__(self, marca, resolucao, seguranca):
        super().__init__(marca, resolucao)
        self.seguranca = seguranca

    def tirar_foto(self, camera_a_utilizar):
        print(f'Foto tirada com aparelho da marca {self.marca} e com a resolução de {
              self.resolução} megapixels, utilizando a câmera {camera_a_utilizar}, com a segurança de {self.seguranca}')


Seguranca = Camera_Seguranca('Apple', '16MP', 'Nível 10')
Seguranca.tirar_foto(2)

print(issubclass(Camera_Seguranca, Camera))
print(issubclass(Camera_Celular, Camera))

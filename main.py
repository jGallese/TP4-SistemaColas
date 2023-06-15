from PyQt5.QtWidgets import *
from ui_tp4 import *
import sys
from generadores.exponencial import *
from generadores.uniforme import *


class AppWin(QMainWindow, Ui_MainWindow):

    def __init__(self):

        QMainWindow.__init__(self)
        self.setupUi(self)  # Se genera la interfaz llamando al metodo setupUi

    def tipoCliente(rnd):
        if (rnd <= 0.44):
            tipo = "ventanilla salida inmediata cercania"

        elif (rnd <= 0.49):
            tipo = "maquina expendedora salida inmediata cercania"
        elif (rnd <= 0.54):
            tipo = "maquina expendedora salida inmediata interprovincial"
        elif (rnd <= 0.79):
            tipo = "ventanilla salida inmediata interprovincial"
        elif (rnd <= 0.99):
            tipo = "venta anticipada"
        return tipo

    def generarProxLlegadaCritica(reloj, media):
        rnd, exp = exponencial(media)
        return rnd, exp, reloj+exp

    def ordenarPrimero(val):
        return val[0]

    def determinarProximoEvento(self, proxEventos: list):
        proxEventos.sort(key=self.ordenarPrimero)
        hora, tipo = proxEventos[0]
        proxEventos.pop(0)
        return hora, tipo

    def simulacion(self):
        cantSimulaciones = int(self.lineEdit.text())
        lineasAMostrar = int(self.lineEdit_2.text())
        horaInicioTraficoModerado = int(self.lineEdit_3.text())
        horaFinTraficoModerado = int(self.lineEdit_4.text())
        horaFinTraficoCritico = int(self.lineEdit_5.text())
        horaInicioTraficoCritico = int(self.lineEdit_6.text())
        lineasAMostrarDesde = int(self.lineEdit_7.text())
        llegadaPasajerosHModMinimo = int(self.lineEdit_8.text())
        llegadaPasajerosHModMaximo = int(self.lineEdit_9.text())
        llegadaPasajerosHCriticoExpNeg = int(self.lineEdit_10.text())
        finAtencionCercaniaVentanillaExpNeg = int(self.lineEdit_11.text())
        finAtencionCercaniaMaqDisp = int(self.lineEdit_12.text())
        finAtencionVentaAnticipadaVentanillaExpNeg = int(
            self.lineEdit_13.text())
        finAtencionInterprovincialVentanillaExpNeg = int(
            self.lineEdit_14.text())
        finAtencionInterprovincialMaqDispExpNeg = int(self.lineEdit_15.text())

        # Eventos
        evento = "inicio"
        relojActual = 0
        #relojAnterior = 0
        horaDia = 0
        proxEventos = [(0, "")]

        # Ventanilla venta anticipada
        colaVentaAnticipada = []
        estadoVentanilla1VentaAnticipada = "libre"
        estadoVentanilla2VentaAnticipada = "libre"

        # Maquina dispensadora
        colaMaquinaDispensadora = []
        estadoMaquinaDispensadora = "libre"

        # Ventanilla salida inmediata
        estadoVentanilla1SalidaInmediata = "libre"
        estadoVentanilla2SalidaInmediata = "libre"
        colaSalidaInmediata = []

        # contadores
        contadorColaSalidaInmediata = 0
        contadorColaVentaAnticipada = 0
        contadorColaMaqDisp = 0
        contadorAbandonoVentaAnticipada = 0
        contadorTotalClientes = 0
        contadorTotalVentaAnticipada = 0

        # ACUMULADORES
        acumuladorTiempoLibreMaquinaDispensadora = 0
        acumuladorTiempoEsperaColaSalidaInmediata = 0
        acumuladorTiempoEsperaColaVentaAnticipada = 0
        acumuladorTiempoEsperaColaMaquinaDispensadora = 0

        # tiempoPromEsperaColas = self.lineEdit_16.setText()
        # cantidadMaxClientesColas = int(self.lineEdit_17.text())
        # porcAbandonoColaVentaAnticipada = int(self.lineEdit_18.text())
        # porcTiempoLibreMaqDisp = int(self.lineEdit_19.text())

        for i in range(cantSimulaciones):
            if (evento == "inicio"):
                horaDia = horaInicioTraficoCritico * 60
                rndHora, exp, hora = self.generarProxLlegadaCritica(
                    relojActual, llegadaPasajerosHCriticoExpNeg)
                proxEventos.append((hora, "llegada cliente"))
                self.cargar(evento, relojActual)
            elif (evento == "llegada cliente"):
                rndTipoCliente = random.random()
                tipoCliente = self.tipoCliente()
                # horaDia = horaDia + relojActual - relojAnterior
                pass
            elif (evento == "fin atencion cercania en ventanilla"):
                pass
            elif (evento == "fin atencion cercania en maquina dispensadora"):
                pass
            elif (evento == "fin atencion interprovincial en ventanilla"):
                pass
            elif (evento == "fin atencion interprovincial en maquina dispensadora"):
                pass
            elif (evento == "fin atencion venta anticipada"):
                pass
            elif (evento == "fin simulacion"):
                pass

    def abandonoCola(colaVentaAnticipada, ):
        pass

    def cargar(self, evento, reloj, horaDia):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)  # create an instance of the application
    appWin = AppWin()  # create an instance of a window
    appWin.show()  # to make the window visible
    app.exec()  # to start up the event loop
    app = QApplication(sys.argv)  # create an instance of the application
    appWin = AppWin()  # create an instance of a window
    appWin.show()  # to make the window visible
    app.exec()  # to start up the event loop

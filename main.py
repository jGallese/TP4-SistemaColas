from PyQt5.QtWidgets import *
from ui_tp4 import *
import sys
from generadores.exponencial import *
from generadores.uniforme import *


class AppWin(QMainWindow, Ui_MainWindow):

    def __init__(self):

        QMainWindow.__init__(self)
        self.setupUi(self)  # Se genera la interfaz llamando al metodo setupUi

    def tipoCliente(self, rnd):
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

    def generarProxLlegadaCritica(self, reloj, media):
        rnd, exp = exponencial2(media)
        return rnd, exp, reloj+exp

    def ordenarPrimero(self, val):
        return val[0]

    def determinarProximoEvento(self, proxEventos: list):
        proxEventos.sort(key=self.ordenarPrimero)
        hora, tipo = proxEventos[0]
        proxEventos.pop(0)
        return hora, tipo

    def simulacion(self):
        cantSimulaciones = int(self.lineEdit.text())
        lineasAMostrar = int(self.lineEdit_2.text())
        lineasAMostrarDesde = int(self.lineEdit_7.text())
        horaInicioTraficoModerado = int(self.lineEdit_3.text())
        horaFinTraficoModerado = int(self.lineEdit_4.text())
        horaFinTraficoCritico = int(self.lineEdit_5.text())
        horaInicioTraficoCritico = int(self.lineEdit_6.text())
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

        indice = 0
        clientes = []
        # Eventos
        evento = "inicio"
        relojActual = 0
        #relojAnterior = 0
        horaDia = 0
        proxEventos = [(0, "")]

        # Ventanilla venta anticipada
        colaVentaAnticipada = []
        estadoVentanillaVentaAnticipada1 = "libre"
        estadoVentanillaVentaAnticipada2 = "libre"

        # Maquina dispensadora
        colaMaquinaDispensadora = []
        estadoMaquinaDispensadora = "libre"

        # Ventanilla salida inmediata
        estadoVentanillaSalidaInmediata1 = "libre"
        estadoVentanillaSalidaInmediata2 = "libre"
        colaSalidaInmediata = []

        # contadores
        horaInicioTiempoLibreMaqDis = 0
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
                if (lineasAMostrarDesde <= indice and indice <= lineasAMostrarDesde + lineasAMostrar):
                    self.cargar(indice - lineasAMostrarDesde, evento, relojActual, horaDia, rndHora, exp, hora, "", "", "", "", "", "", "", "", "", "", "", "", "", str(len(colaSalidaInmediata)), estadoVentanillaSalidaInmediata1, estadoVentanillaSalidaInmediata2, str(len(colaVentaAnticipada)), estadoVentanillaVentaAnticipada1, estadoVentanillaVentaAnticipada2, str(len(colaMaquinaDispensadora)), estadoMaquinaDispensadora, str(horaInicioTiempoLibreMaqDis),
                                str(contadorColaSalidaInmediata), str(contadorColaVentaAnticipada), str(contadorColaMaqDisp), str(contadorTotalClientes), str(contadorTotalVentaAnticipada), str(acumuladorTiempoLibreMaquinaDispensadora), str(acumuladorTiempoEsperaColaSalidaInmediata), str(acumuladorTiempoEsperaColaVentaAnticipada), str(acumuladorTiempoEsperaColaMaquinaDispensadora), clientes)
                hora, evento = self.determinarProximoEvento(proxEventos)
            elif (evento == "llegada cliente"):
                rndTipoCliente = random.random()
                tipoCliente = self.tipoCliente(rndTipoCliente)

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

            indice += 1

    def abandonoCola(colaVentaAnticipada, ):
        pass

    def cargar(self, indice, evento, reloj, horaDia, rndLlegada, tiempoLlegada, horaLlegada, rndTipoCliente, tipoCliente, rndFinAtencionInmediataEnVentanilla, tiempoFinAtencionInmediataVent, finAtencionInmediataVent1, finAtencionInmediataVent2, RNDFinAtencionInmediataMaqDis, tiempoFinAtencionInmediataMaqDis,
               finAtencionInmediataMaqDis, rndFinAtencionVentaAnticipadaVentanilla, tiempoFinAtencionVentaAnticipadaVentanilla, finAtencionVentaAnticipadaVentanilla1, finAtencionVentaAnticipadaVentanilla2,
               colaVentanillaSalidaInmediata, estadoVentanillaInmediata1, estadoVentanillaInmediata2, colaVentanillaAnticipada, estadoVentanillaAnticipada1, estadoVentanillaAnticipada2, colaMaqDis, estadoMaqDis, horaInicioTiempoLibreMaqDis,
               contColaSalidaInmediata, contColaVentaAnticipada, contColaMaqDis, contadorTotalClientes, contadorTotalClientesVentaAnticipada, acumTiempoLibreMaqDis, acumTiempoEsperaColaSalidaInmediata, acumTiempoEsperaColaVentaAnticipada, acumTiempoEsperaMaqDis, clientes):
        # clientes
        self.tableWidget.insertRow(indice)
        self.tableWidget.setItem(
            indice, 0, QtWidgets.QTableWidgetItem(str(evento)))
        self.tableWidget.setItem(
            indice, 1, QtWidgets.QTableWidgetItem(str(reloj)))
        self.tableWidget.setItem(
            indice, 2, QtWidgets.QTableWidgetItem(str(horaDia)))
        self.tableWidget.setItem(
            indice, 3, QtWidgets.QTableWidgetItem(str(rndLlegada)))
        self.tableWidget.setItem(
            indice, 4, QtWidgets.QTableWidgetItem(str(tiempoLlegada)))
        self.tableWidget.setItem(
            indice, 5, QtWidgets.QTableWidgetItem(str(horaLlegada)))
        self.tableWidget.setItem(
            indice, 6, QtWidgets.QTableWidgetItem(str(rndTipoCliente)))
        self.tableWidget.setItem(
            indice, 7, QtWidgets.QTableWidgetItem(str(tipoCliente)))
        self.tableWidget.setItem(indice, 8, QtWidgets.QTableWidgetItem(
            str(rndFinAtencionInmediataEnVentanilla)))
        self.tableWidget.setItem(indice, 9, QtWidgets.QTableWidgetItem(
            str(tiempoFinAtencionInmediataVent)))
        self.tableWidget.setItem(indice, 10, QtWidgets.QTableWidgetItem(
            str(finAtencionInmediataVent1)))
        self.tableWidget.setItem(indice, 11, QtWidgets.QTableWidgetItem(
            str(finAtencionInmediataVent2)))
        self.tableWidget.setItem(indice, 12, QtWidgets.QTableWidgetItem(
            str(RNDFinAtencionInmediataMaqDis)))
        self.tableWidget.setItem(indice, 13, QtWidgets.QTableWidgetItem(
            str(tiempoFinAtencionInmediataMaqDis)))
        self.tableWidget.setItem(indice, 14, QtWidgets.QTableWidgetItem(
            str(finAtencionInmediataMaqDis)))
        self.tableWidget.setItem(indice, 15, QtWidgets.QTableWidgetItem(
            str(rndFinAtencionVentaAnticipadaVentanilla)))
        self.tableWidget.setItem(indice, 16, QtWidgets.QTableWidgetItem(
            str(tiempoFinAtencionVentaAnticipadaVentanilla)))
        self.tableWidget.setItem(indice, 17, QtWidgets.QTableWidgetItem(
            str(finAtencionVentaAnticipadaVentanilla1)))
        self.tableWidget.setItem(indice, 18, QtWidgets.QTableWidgetItem(
            str(finAtencionVentaAnticipadaVentanilla2)))
        self.tableWidget.setItem(indice, 19, QtWidgets.QTableWidgetItem(
            str(colaVentanillaSalidaInmediata)))
        self.tableWidget.setItem(indice, 20, QtWidgets.QTableWidgetItem(
            str(estadoVentanillaInmediata1)))
        self.tableWidget.setItem(indice, 21, QtWidgets.QTableWidgetItem(
            str(estadoVentanillaInmediata2)))
        self.tableWidget.setItem(
            indice, 22, QtWidgets.QTableWidgetItem(str(colaVentanillaAnticipada)))
        self.tableWidget.setItem(indice, 23, QtWidgets.QTableWidgetItem(
            str(estadoVentanillaAnticipada1)))
        self.tableWidget.setItem(indice, 24, QtWidgets.QTableWidgetItem(
            str(estadoVentanillaAnticipada2)))
        self.tableWidget.setItem(
            indice, 25, QtWidgets.QTableWidgetItem(str(colaMaqDis)))
        self.tableWidget.setItem(
            indice, 26, QtWidgets.QTableWidgetItem(str(estadoMaqDis)))
        self.tableWidget.setItem(indice, 27, QtWidgets.QTableWidgetItem(
            str(horaInicioTiempoLibreMaqDis)))
        self.tableWidget.setItem(
            indice, 28, QtWidgets.QTableWidgetItem(str(contColaSalidaInmediata)))
        self.tableWidget.setItem(
            indice, 29, QtWidgets.QTableWidgetItem(str(contColaVentaAnticipada)))
        self.tableWidget.setItem(
            indice, 30, QtWidgets.QTableWidgetItem(str(contColaMaqDis)))
        self.tableWidget.setItem(
            indice, 31, QtWidgets.QTableWidgetItem(str(contadorTotalClientes)))
        self.tableWidget.setItem(indice, 32, QtWidgets.QTableWidgetItem(
            str(contadorTotalClientesVentaAnticipada)))
        self.tableWidget.setItem(
            indice, 33, QtWidgets.QTableWidgetItem(str(acumTiempoLibreMaqDis)))
        self.tableWidget.setItem(indice, 34, QtWidgets.QTableWidgetItem(
            str(acumTiempoEsperaColaSalidaInmediata)))
        self.tableWidget.setItem(indice, 35, QtWidgets.QTableWidgetItem(
            str(acumTiempoEsperaColaVentaAnticipada)))
        self.tableWidget.setItem(
            indice, 36, QtWidgets.QTableWidgetItem(str(acumTiempoEsperaMaqDis)))


if __name__ == '__main__':
    app = QApplication(sys.argv)  # create an instance of the application
    appWin = AppWin()  # create an instance of a window
    appWin.show()  # to make the window visible
    app.exec()  # to start up the event loop
    app = QApplication(sys.argv)  # create an instance of the application
    appWin = AppWin()  # create an instance of a window
    appWin.show()  # to make the window visible
    app.exec()  # to start up the event loop

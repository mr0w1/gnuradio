#!/usr/bin/env python2
##################################################
# GNU Radio Python Flow Graph
# Title: WBFM 2 Channel
# Generated: Sun Jun 19 01:12:56 2016
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt4 import Qt
from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import osmosdr
import sip
import sys
import time


class wbfm_2ch(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "WBFM 2 Channel")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("WBFM 2 Channel")
        try:
             self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
             pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "wbfm_2ch")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.radio_freq = radio_freq = 100
        self.samp_rate = samp_rate = 240e4
        self.rf_gain = rf_gain = 10
        self.freq = freq = radio_freq * 1000000
        self.ch2volume = ch2volume = 5
        self.ch2squelch = ch2squelch = -30
        self.ch2mute = ch2mute = 1
        self.ch2freq = ch2freq = radio_freq
        self.ch1volume = ch1volume = 5
        self.ch1squelch = ch1squelch = -30
        self.ch1mute = ch1mute = 1
        self.ch1freq = ch1freq = radio_freq

        ##################################################
        # Blocks
        ##################################################
        self.ch2 = Qt.QTabWidget()
        self.ch2_widget_0 = Qt.QWidget()
        self.ch2_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.ch2_widget_0)
        self.ch2_grid_layout_0 = Qt.QGridLayout()
        self.ch2_layout_0.addLayout(self.ch2_grid_layout_0)
        self.ch2.addTab(self.ch2_widget_0, "Ch 2")
        self.top_grid_layout.addWidget(self.ch2, 2,1,1,1)
        self.ch1 = Qt.QTabWidget()
        self.ch1_widget_0 = Qt.QWidget()
        self.ch1_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.ch1_widget_0)
        self.ch1_grid_layout_0 = Qt.QGridLayout()
        self.ch1_layout_0.addLayout(self.ch1_grid_layout_0)
        self.ch1.addTab(self.ch1_widget_0, "Ch 1")
        self.top_grid_layout.addWidget(self.ch1, 2,0,1,1)
        self._rf_gain_range = Range(0, 50, 1, 10, 200)
        self._rf_gain_win = RangeWidget(self._rf_gain_range, self.set_rf_gain, "RF Gain", "counter_slider", float)
        self.top_grid_layout.addWidget(self._rf_gain_win, 1,0,1,2)
        self._ch2volume_range = Range(0, 10, 1, 5, 200)
        self._ch2volume_win = RangeWidget(self._ch2volume_range, self.set_ch2volume, "Ch2 Volume", "counter_slider", float)
        self.ch2_grid_layout_0.addWidget(self._ch2volume_win, 1,0,1,2)
        self._ch2squelch_range = Range(-70, 0, 10, -30, 200)
        self._ch2squelch_win = RangeWidget(self._ch2squelch_range, self.set_ch2squelch, "Ch2 Squelch", "counter_slider", int)
        self.ch2_grid_layout_0.addWidget(self._ch2squelch_win, 2,0,1,2)
        _ch2mute_check_box = Qt.QCheckBox("Mute")
        self._ch2mute_choices = {True: 0, False: 1}
        self._ch2mute_choices_inv = dict((v,k) for k,v in self._ch2mute_choices.iteritems())
        self._ch2mute_callback = lambda i: Qt.QMetaObject.invokeMethod(_ch2mute_check_box, "setChecked", Qt.Q_ARG("bool", self._ch2mute_choices_inv[i]))
        self._ch2mute_callback(self.ch2mute)
        _ch2mute_check_box.stateChanged.connect(lambda i: self.set_ch2mute(self._ch2mute_choices[bool(i)]))
        self.ch2_grid_layout_0.addWidget(_ch2mute_check_box, 0,1,1,1)
        self._ch2freq_tool_bar = Qt.QToolBar(self)
        self._ch2freq_tool_bar.addWidget(Qt.QLabel("Ch2 Freq"+": "))
        self._ch2freq_line_edit = Qt.QLineEdit(str(self.ch2freq))
        self._ch2freq_tool_bar.addWidget(self._ch2freq_line_edit)
        self._ch2freq_line_edit.returnPressed.connect(
        	lambda: self.set_ch2freq(eng_notation.str_to_num(str(self._ch2freq_line_edit.text().toAscii()))))
        self.ch2_grid_layout_0.addWidget(self._ch2freq_tool_bar, 0,0,1,1)
        self._ch1volume_range = Range(0, 10, 1, 5, 200)
        self._ch1volume_win = RangeWidget(self._ch1volume_range, self.set_ch1volume, "Ch1 Volume", "counter_slider", float)
        self.ch1_grid_layout_0.addWidget(self._ch1volume_win, 1,0,1,2)
        self._ch1squelch_range = Range(-70, 0, 10, -30, 200)
        self._ch1squelch_win = RangeWidget(self._ch1squelch_range, self.set_ch1squelch, "Ch1 Squelch", "counter_slider", int)
        self.ch1_grid_layout_0.addWidget(self._ch1squelch_win, 2,0,1,2)
        _ch1mute_check_box = Qt.QCheckBox("Mute")
        self._ch1mute_choices = {True: 0, False: 1}
        self._ch1mute_choices_inv = dict((v,k) for k,v in self._ch1mute_choices.iteritems())
        self._ch1mute_callback = lambda i: Qt.QMetaObject.invokeMethod(_ch1mute_check_box, "setChecked", Qt.Q_ARG("bool", self._ch1mute_choices_inv[i]))
        self._ch1mute_callback(self.ch1mute)
        _ch1mute_check_box.stateChanged.connect(lambda i: self.set_ch1mute(self._ch1mute_choices[bool(i)]))
        self.ch1_grid_layout_0.addWidget(_ch1mute_check_box, 0,1,1,1)
        self._ch1freq_tool_bar = Qt.QToolBar(self)
        self._ch1freq_tool_bar.addWidget(Qt.QLabel("Ch1 Freq"+": "))
        self._ch1freq_line_edit = Qt.QLineEdit(str(self.ch1freq))
        self._ch1freq_tool_bar.addWidget(self._ch1freq_line_edit)
        self._ch1freq_line_edit.returnPressed.connect(
        	lambda: self.set_ch1freq(eng_notation.str_to_num(str(self._ch1freq_line_edit.text().toAscii()))))
        self.ch1_grid_layout_0.addWidget(self._ch1freq_tool_bar, 0,0,1,1)
        self.rtlsdr_source_0 = osmosdr.source( args="numchan=" + str(1) + " " + "" )
        self.rtlsdr_source_0.set_sample_rate(samp_rate)
        self.rtlsdr_source_0.set_center_freq(freq, 0)
        self.rtlsdr_source_0.set_freq_corr(0, 0)
        self.rtlsdr_source_0.set_dc_offset_mode(0, 0)
        self.rtlsdr_source_0.set_iq_balance_mode(0, 0)
        self.rtlsdr_source_0.set_gain_mode(False, 0)
        self.rtlsdr_source_0.set_gain(rf_gain, 0)
        self.rtlsdr_source_0.set_if_gain(20, 0)
        self.rtlsdr_source_0.set_bb_gain(20, 0)
        self.rtlsdr_source_0.set_antenna("", 0)
        self.rtlsdr_source_0.set_bandwidth(0, 0)
          
        self.rational_resampler_xxx_2_0 = filter.rational_resampler_ccc(
                interpolation=400000,
                decimation=2400000,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_2 = filter.rational_resampler_ccc(
                interpolation=400000,
                decimation=2400000,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_1_0 = filter.rational_resampler_fff(
                interpolation=48,
                decimation=50,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_1 = filter.rational_resampler_fff(
                interpolation=48,
                decimation=50,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_0_0 = filter.rational_resampler_ccc(
                interpolation=500000,
                decimation=2400000,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=500000,
                decimation=2400000,
                taps=None,
                fractional_bw=None,
        )
        self._radio_freq_tool_bar = Qt.QToolBar(self)
        self._radio_freq_tool_bar.addWidget(Qt.QLabel("Frequency (MHz)"+": "))
        self._radio_freq_line_edit = Qt.QLineEdit(str(self.radio_freq))
        self._radio_freq_tool_bar.addWidget(self._radio_freq_line_edit)
        self._radio_freq_line_edit.returnPressed.connect(
        	lambda: self.set_radio_freq(eng_notation.str_to_num(str(self._radio_freq_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._radio_freq_tool_bar, 0,0,1,2)
        self.qtgui_waterfall_sink_x_0 = qtgui.waterfall_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	freq, #fc
        	samp_rate, #bw
        	"", #name
                1 #number of inputs
        )
        self.qtgui_waterfall_sink_x_0.set_update_time(0.10)
        self.qtgui_waterfall_sink_x_0.enable_grid(False)
        
        if not True:
          self.qtgui_waterfall_sink_x_0.disable_legend()
        
        if complex == type(float()):
          self.qtgui_waterfall_sink_x_0.set_plot_pos_half(not True)
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        colors = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_waterfall_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_waterfall_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_waterfall_sink_x_0.set_color_map(i, colors[i])
            self.qtgui_waterfall_sink_x_0.set_line_alpha(i, alphas[i])
        
        self.qtgui_waterfall_sink_x_0.set_intensity_range(-100, 10)
        
        self._qtgui_waterfall_sink_x_0_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_waterfall_sink_x_0_win, 3,0,1,2)
        self.qtgui_freq_sink_x_0_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	ch2freq, #fc
        	400000, #bw
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0_0.set_y_axis(-100, 10)
        self.qtgui_freq_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0_0.enable_grid(False)
        self.qtgui_freq_sink_x_0_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0_0.enable_control_panel(False)
        
        if not False:
          self.qtgui_freq_sink_x_0_0.disable_legend()
        
        if complex == type(float()):
          self.qtgui_freq_sink_x_0_0.set_plot_pos_half(not True)
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_freq_sink_x_0_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.ch2_grid_layout_0.addWidget(self._qtgui_freq_sink_x_0_0_win, 3,0,1,2)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	ch1freq, #fc
        	400000, #bw
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-100, 10)
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)
        
        if not False:
          self.qtgui_freq_sink_x_0.disable_legend()
        
        if complex == type(float()):
          self.qtgui_freq_sink_x_0.set_plot_pos_half(not True)
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.pyqwidget(), Qt.QWidget)
        self.ch1_grid_layout_0.addWidget(self._qtgui_freq_sink_x_0_win, 3,0,1,2)
        self.low_pass_filter_0_0 = filter.fir_filter_ccf(1, firdes.low_pass(
        	1, 500000, 100e3, 8000, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0 = filter.fir_filter_ccf(1, firdes.low_pass(
        	1, 500000, 100e3, 8000, firdes.WIN_HAMMING, 6.76))
        self.freq_xlating_fft_filter_ccc_0_0 = filter.freq_xlating_fft_filter_ccc(1, (firdes.low_pass(1,samp_rate,200000,10000)), (ch2freq * 1000000) - freq, samp_rate)
        self.freq_xlating_fft_filter_ccc_0_0.set_nthreads(1)
        self.freq_xlating_fft_filter_ccc_0_0.declare_sample_delay(0)
        self.freq_xlating_fft_filter_ccc_0 = filter.freq_xlating_fft_filter_ccc(1, (firdes.low_pass(1,samp_rate,200000,10000)), (ch1freq * 1000000) - freq, samp_rate)
        self.freq_xlating_fft_filter_ccc_0.set_nthreads(1)
        self.freq_xlating_fft_filter_ccc_0.declare_sample_delay(0)
        self.blocks_multiply_const_vxx_1_0 = blocks.multiply_const_vff((ch2mute, ))
        self.blocks_multiply_const_vxx_1 = blocks.multiply_const_vff((ch1mute, ))
        self.blocks_multiply_const_vxx_0_0 = blocks.multiply_const_vff((ch2volume, ))
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((ch1volume, ))
        self.audio_sink_0_0 = audio.sink(48000, "", True)
        self.audio_sink_0 = audio.sink(48000, "", True)
        self.analog_wfm_rcv_0_0 = analog.wfm_rcv(
        	quad_rate=500000,
        	audio_decimation=10,
        )
        self.analog_wfm_rcv_0 = analog.wfm_rcv(
        	quad_rate=500000,
        	audio_decimation=10,
        )
        self.analog_pwr_squelch_xx_0_0 = analog.pwr_squelch_cc(ch2squelch, 1e-4, 0, True)
        self.analog_pwr_squelch_xx_0 = analog.pwr_squelch_cc(ch1squelch, 1e-4, 0, True)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_pwr_squelch_xx_0, 0), (self.rational_resampler_xxx_0, 0))    
        self.connect((self.analog_pwr_squelch_xx_0_0, 0), (self.rational_resampler_xxx_0_0, 0))    
        self.connect((self.analog_wfm_rcv_0, 0), (self.rational_resampler_xxx_1, 0))    
        self.connect((self.analog_wfm_rcv_0_0, 0), (self.rational_resampler_xxx_1_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_multiply_const_vxx_1, 0))    
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.blocks_multiply_const_vxx_1_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.audio_sink_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_1_0, 0), (self.audio_sink_0_0, 0))    
        self.connect((self.freq_xlating_fft_filter_ccc_0, 0), (self.analog_pwr_squelch_xx_0, 0))    
        self.connect((self.freq_xlating_fft_filter_ccc_0, 0), (self.rational_resampler_xxx_2, 0))    
        self.connect((self.freq_xlating_fft_filter_ccc_0_0, 0), (self.analog_pwr_squelch_xx_0_0, 0))    
        self.connect((self.freq_xlating_fft_filter_ccc_0_0, 0), (self.rational_resampler_xxx_2_0, 0))    
        self.connect((self.low_pass_filter_0, 0), (self.analog_wfm_rcv_0, 0))    
        self.connect((self.low_pass_filter_0_0, 0), (self.analog_wfm_rcv_0_0, 0))    
        self.connect((self.rational_resampler_xxx_0, 0), (self.low_pass_filter_0, 0))    
        self.connect((self.rational_resampler_xxx_0_0, 0), (self.low_pass_filter_0_0, 0))    
        self.connect((self.rational_resampler_xxx_1, 0), (self.blocks_multiply_const_vxx_0, 0))    
        self.connect((self.rational_resampler_xxx_1_0, 0), (self.blocks_multiply_const_vxx_0_0, 0))    
        self.connect((self.rational_resampler_xxx_2, 0), (self.qtgui_freq_sink_x_0, 0))    
        self.connect((self.rational_resampler_xxx_2_0, 0), (self.qtgui_freq_sink_x_0_0, 0))    
        self.connect((self.rtlsdr_source_0, 0), (self.freq_xlating_fft_filter_ccc_0, 0))    
        self.connect((self.rtlsdr_source_0, 0), (self.freq_xlating_fft_filter_ccc_0_0, 0))    
        self.connect((self.rtlsdr_source_0, 0), (self.qtgui_waterfall_sink_x_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "wbfm_2ch")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_radio_freq(self):
        return self.radio_freq

    def set_radio_freq(self, radio_freq):
        self.radio_freq = radio_freq
        self.set_ch1freq(self.radio_freq)
        self.set_ch2freq(self.radio_freq)
        self.set_freq(self.radio_freq * 1000000)
        Qt.QMetaObject.invokeMethod(self._radio_freq_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.radio_freq)))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.freq_xlating_fft_filter_ccc_0.set_taps((firdes.low_pass(1,self.samp_rate,200000,10000)))
        self.freq_xlating_fft_filter_ccc_0_0.set_taps((firdes.low_pass(1,self.samp_rate,200000,10000)))
        self.qtgui_waterfall_sink_x_0.set_frequency_range(self.freq, self.samp_rate)
        self.rtlsdr_source_0.set_sample_rate(self.samp_rate)

    def get_rf_gain(self):
        return self.rf_gain

    def set_rf_gain(self, rf_gain):
        self.rf_gain = rf_gain
        self.rtlsdr_source_0.set_gain(self.rf_gain, 0)

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self.freq_xlating_fft_filter_ccc_0.set_center_freq((self.ch1freq * 1000000) - self.freq)
        self.freq_xlating_fft_filter_ccc_0_0.set_center_freq((self.ch2freq * 1000000) - self.freq)
        self.qtgui_waterfall_sink_x_0.set_frequency_range(self.freq, self.samp_rate)
        self.rtlsdr_source_0.set_center_freq(self.freq, 0)

    def get_ch2volume(self):
        return self.ch2volume

    def set_ch2volume(self, ch2volume):
        self.ch2volume = ch2volume
        self.blocks_multiply_const_vxx_0_0.set_k((self.ch2volume, ))

    def get_ch2squelch(self):
        return self.ch2squelch

    def set_ch2squelch(self, ch2squelch):
        self.ch2squelch = ch2squelch
        self.analog_pwr_squelch_xx_0_0.set_threshold(self.ch2squelch)

    def get_ch2mute(self):
        return self.ch2mute

    def set_ch2mute(self, ch2mute):
        self.ch2mute = ch2mute
        self._ch2mute_callback(self.ch2mute)
        self.blocks_multiply_const_vxx_1_0.set_k((self.ch2mute, ))

    def get_ch2freq(self):
        return self.ch2freq

    def set_ch2freq(self, ch2freq):
        self.ch2freq = ch2freq
        Qt.QMetaObject.invokeMethod(self._ch2freq_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.ch2freq)))
        self.freq_xlating_fft_filter_ccc_0_0.set_center_freq((self.ch2freq * 1000000) - self.freq)
        self.qtgui_freq_sink_x_0_0.set_frequency_range(self.ch2freq, 400000)

    def get_ch1volume(self):
        return self.ch1volume

    def set_ch1volume(self, ch1volume):
        self.ch1volume = ch1volume
        self.blocks_multiply_const_vxx_0.set_k((self.ch1volume, ))

    def get_ch1squelch(self):
        return self.ch1squelch

    def set_ch1squelch(self, ch1squelch):
        self.ch1squelch = ch1squelch
        self.analog_pwr_squelch_xx_0.set_threshold(self.ch1squelch)

    def get_ch1mute(self):
        return self.ch1mute

    def set_ch1mute(self, ch1mute):
        self.ch1mute = ch1mute
        self._ch1mute_callback(self.ch1mute)
        self.blocks_multiply_const_vxx_1.set_k((self.ch1mute, ))

    def get_ch1freq(self):
        return self.ch1freq

    def set_ch1freq(self, ch1freq):
        self.ch1freq = ch1freq
        Qt.QMetaObject.invokeMethod(self._ch1freq_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.ch1freq)))
        self.freq_xlating_fft_filter_ccc_0.set_center_freq((self.ch1freq * 1000000) - self.freq)
        self.qtgui_freq_sink_x_0.set_frequency_range(self.ch1freq, 400000)


if __name__ == '__main__':
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        Qt.QApplication.setGraphicsSystem(gr.prefs().get_string('qtgui','style','raster'))
    qapp = Qt.QApplication(sys.argv)
    tb = wbfm_2ch()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()
    tb = None  # to clean up Qt widgets

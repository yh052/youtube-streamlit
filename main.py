import streamlit as st
import numpy as np
import pandas as pd 
from PIL import Image
import time


st.title('Streamlit 超入門')

st.write('プログレスバーの表示')
'Start!!'

Latest_iteration = st.empty()
bar = st.progress(0)

import time 
for i in range(100):
    Latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'Done!!!!'

left_column, right_column, = st.beta_columns(2)
button =left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander = st.beta_expander('問い合わせ')
expander.write('問い合わせ内容を書く')

# text = st.text_input('あなたの趣味を教えてください')
# condition = st.slider('あなたの今の調子は？',0,100,50)

# 'あなたの趣味:' , text
# 'コンディション:' , condition


# if st.checkbox('Show Image'):
#     img = Image.open('muji.jpg') 
#     st.image(img, caption='Yuri', use_column_width=True)

Add-Type -TypeDefinition '
using System;
using System.ComponentModel;
using System.Runtime.InteropServices;

public static class ScreenReaderFixUtil
{
    public static bool IsScreenReaderActive()
    {
        var ptr = IntPtr.Zero;
        try
        {
            ptr = Marshal.AllocHGlobal(sizeof(int));
            int hr = Interop.SystemParametersInfo(
                Interop.SPI_GETSCREENREADER,
                sizeof(int),
                ptr,
                0);

            if (hr == 0)
            {
                throw new Win32Exception(Marshal.GetLastWin32Error());
            }

            return Marshal.ReadInt32(ptr) != 0;
        }
        finally
        {
            if (ptr != IntPtr.Zero)
            {
                Marshal.FreeHGlobal(ptr);
            }
        }
    }

    public static void SetScreenReaderActiveStatus(bool isActive)
    {
        int hr = Interop.SystemParametersInfo(
            Interop.SPI_SETSCREENREADER,
            isActive ? 1u : 0u,
            IntPtr.Zero,
            Interop.SPIF_SENDCHANGE);

        if (hr == 0)
        {
            throw new Win32Exception(Marshal.GetLastWin32Error());
        }
    }

    private static class Interop
    {
        public const int SPIF_SENDCHANGE = 0x0002;

        public const int SPI_GETSCREENREADER = 0x0046;

        public const int SPI_SETSCREENREADER = 0x0047;

        [DllImport("user32", SetLastError = true, CharSet = CharSet.Unicode)]
        public static extern int SystemParametersInfo(
            uint uiAction,
            uint uiParam,
            IntPtr pvParam,
            uint fWinIni);
    }
}'

if ([ScreenReaderFixUtil]::IsScreenReaderActive()) {
    [ScreenReaderFixUtil]::SetScreenReaderActiveStatus($false)
}
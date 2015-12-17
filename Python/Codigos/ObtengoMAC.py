__author__ = 'juan'

manifiesto = open("/home/juan/Escritorio/manifiesto","a", 0)
manifiesto.write( "192.168.122.254 {\n"
                  "       include apache;\n"
                  "}");

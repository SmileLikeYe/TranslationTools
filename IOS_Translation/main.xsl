<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:sap="urn:SAPBusinessOne:formatdefinition:extension">
<xsl:output method="text" encoding="utf-8"/>
<xsl:template match="text()" />
<xsl:template match="/" xmlns:s0="www.sap.com/slim">
<xsl:variable name="var1_root" select="." />
<xsl:for-each select="$var1_root/s0:slim">
<xsl:for-each select="s0:body">
<xsl:for-each select="s0:loGrp">
<xsl:for-each select="s0:lo">
<xsl:variable name="var5_const" select="'&quot;'" />
<xsl:variable name="var6_const" select="1" />
<xsl:variable name="var7_const" select="' '" />
<xsl:variable name="var8_const" select="true()" />
<xsl:variable name="var9_const" select="true()" />
<xsl:variable name="var10_padding-align" select="'&quot;'" />
<xsl:value-of select="$var10_padding-align" />
<xsl:for-each select="@tK">
<xsl:variable name="var12_tK" select="." />
<xsl:value-of select="$var12_tK" />
</xsl:for-each>
<xsl:variable name="var13_const" select="'&quot;=&quot;'" />
<xsl:value-of select="$var13_const" />
<xsl:for-each select="s0:loC">
<xsl:variable name="var15_loC" select="." />
<xsl:variable name="var16_const" select="1" />
<xsl:variable name="var17_loC" select="." />
<xsl:variable name="var18_string-length" select="string-length($var17_loC)" />
<xsl:variable name="var19_const" select="0" />
<xsl:variable name="var20_subtract" select="$var18_string-length - $var19_const" />
<xsl:variable name="var21_substring" select="substring($var15_loC,$var16_const,$var20_subtract)" />
<xsl:value-of select="$var21_substring" />
</xsl:for-each>
<xsl:variable name="var22_const" select="'&quot;'" />
<xsl:variable name="var23_const" select="1" />
<xsl:variable name="var24_const" select="' '" />
<xsl:variable name="var25_const" select="true()" />
<xsl:variable name="var26_const" select="true()" />
<xsl:variable name="var27_padding-align" select="'&quot;;'" />
<xsl:value-of select="$var27_padding-align" />
<xsl:text xml:space="preserve">
</xsl:text>
</xsl:for-each>
</xsl:for-each>
</xsl:for-each>
</xsl:for-each>
</xsl:template>
</xsl:stylesheet>

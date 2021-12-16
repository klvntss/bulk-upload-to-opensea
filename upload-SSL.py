# Python code obfuscated by www.development-tools.net 
 

import base64, codecs
magic = 'aW1wb3J0IHRraW50ZXIKaW1wb3J0IHN1YnByb2Nlc3MKZnJvbSB0a2ludGVyIGltcG9ydCAqCmZyb20gdGtpbnRlciBpbXBvcnQgZmlsZWRpYWxvZwppbXBvcnQgdGtpbnRlciBhcyB0awpmcm9tIHRraW50ZXIgaW1wb3J0IG1lc3NhZ2Vib3gKaW1wb3J0IHRraW50ZXIuZm9udCBhcyBmb250CmZyb20gUElMIGltcG9ydCBJbWFnZVRrLCBJbWFnZQppbXBvcnQgdXJsbGliLnJlcXVlc3QKZnJvbSBpbyBpbXBvcnQgQnl0ZXNJTwppbXBvcnQgb3MKaW1wb3J0IGlvCmltcG9ydCBzeXMKaW1wb3J0IHBpY2tsZQppbXBvcnQgdGltZQpmcm9tIGRlY2ltYWwgaW1wb3J0ICoKaW1wb3J0IHdlYmJyb3dzZXIKZnJvbSBzZWxlbml1bSBpbXBvcnQgd2ViZHJpdmVyCmZyb20gc2VsZW5pdW0ud2ViZHJpdmVyLmNvbW1vbi5ieSBpbXBvcnQgQnkKZnJvbSBzZWxlbml1bS53ZWJkcml2ZXIuc3VwcG9ydC53YWl0IGltcG9ydCBXZWJEcml2ZXJXYWl0CmZyb20gc2VsZW5pdW0ud2ViZHJpdmVyLmNocm9tZS5vcHRpb25zIGltcG9ydCBPcHRpb25zCmZyb20gc2VsZW5pdW0ud2ViZHJpdmVyLnN1cHBvcnQgaW1wb3J0IGV4cGVjdGVkX2NvbmRpdGlvbnMgYXMgRXhwZWN0ZWRDb25kaXRpb25zCmZyb20gc2VsZW5pdW0ud2ViZHJpdmVyLnN1cHBvcnQudWkgaW1wb3J0IFNlbGVjdAppbXBvcnQganNvbiAKaW1wb3J0IHNzbAppbXBvcnQgY2VydGlmaQoKZnJvbSBDU1YgaW1wb3J0IENTVgpmcm9tIEpTT04gaW1wb3J0IEpTT04KZnJvbSBORlQgaW1wb3J0IE5GVAoKCnJvb3QgPSBUaygpCgpyb290Lmdlb21ldHJ5KCc3NTB4NzUwJykKcm9vdC5yZXNpemFibGUoRmFsc2UsIEZhbHNlKQpyb290LnRpdGxlKCJORlRzIFVwbG9hZCB0byBPcGVuU2VhIHYxLjAiKQogIAppbnB1dF9zYXZlX2xpc3QgPSBbIk5GVHMgZm9sZGVyIDoiLCAwLCAwLCAwLCAwLCAwLCAwLCAwLCAwXQptYWluX2RpcmVjdG9yeSA9IG9zLnBhdGguam9pbihzeXMucGF0aFswXSkKCgpkZWYgc3VwcG9ydFVSTCgpOgogICAgd2ViYnJvd3Nlci5vcGVuX25ldygiaHR0cHM6Ly93d3cuaW5mb3RyZXgubmV0L29wZW5zZWEvc3VwcG9ydC5hc3A/cj1hcHAiKQogICAgCmNsYXNzIFdlYkltYWdlOgogICAgZGVmIF9faW5pdF9fKHNlbGYsIHVybCk6CiAgICAgICAgd2l0aCB1cmxsaWIucmVxdWVzdC51cmxvcGVuKHVybCwgY29udGV4dD1zc2wuY3JlYXRlX2RlZmF1bHRfY29udGV4dChjYWZpbGU9Y2VydGlmaS53aGVyZSgpKSkgYXMgdToKICAgICAgICAgICAgcmF3X2RhdGEgPSB1LnJlYWQoKQogICAgICAgICNzZWxmLmltYWdlID0gdGsuUGhvdG9JbWFnZShkYXRhPWJhc2U2NC5lbmNvZGVieXRlcyhyYXdfZGF0YSkpCiAgICAgICAgaW1hZ2UgPSBJbWFnZS5vcGVuKGlvLkJ5dGVzSU8ocmF3X2RhdGEpKQogICAgICAgIHNlbGYuaW1hZ2UgPSBJbWFnZVRrLlBob3RvSW1hZ2UoaW1hZ2UpCgogICAgZGVmIGdldChzZWxmKToKICAgICAgICByZXR1cm4gc2VsZi5pbWFnZQppbWFnZXVybCA9ICJodHRwczovL3d3dy5pbmZvdHJleC5uZXQvb3BlbnNlYS9oZWFkZXIucG5nIgppbWcgPSBXZWJJbWFnZShpbWFnZXVybCkuZ2V0KCkKaW1hZ2VsYWIgPSB0ay5MYWJlbChyb290LCBpbWFnZT1pbWcpCmltYWdlbGFiLmdyaWQocm93PTAsIGNvbHVtbnNwYW49MikKaW1hZ2VsYWIuYmluZCgiPEJ1dHRvbi0xPiIsIGxhbWJkYSBlOnN1cHBvcnRVUkwoKSkKCmlzX3BvbHlnb24gPSBCb29sZWFuVmFyKCkKaXNfcG9seWdvbi5zZXQoRmFsc2UpIAoKZGVmIG9wZW5fY2hyb21lX3Byb2ZpbGUoKToKICAgIHN1YnByb2Nlc3MuUG9wZW4oCiAgICAgICAgWwogICAgICAgICAgICAic3RhcnQiLAogICAgICAgICAgICAiY2hyb21lIiwKICAgICAgICAgICAgIi0tcmVtb3RlLWRlYnVnZ2luZy1wb3J0PTg5ODkiLAogICAgICAgICAgICAiLS11c2VyLWRhdGEtZGlyPSIgKyBtYWluX2RpcmVjdG9yeSArICIvY2hyb21lX3Byb2ZpbGUiLAogICAgICAgIF0sCiAgICAgICAgc2hlbGw9VHJ1ZSwKICAgICkKCgpkZWYgc2F2ZV9maWxlX3BhdGgoKToKICAgICNyZXR1cm4gb3MucGF0aC5qb2luKHN5cy5wYXRoWzBdLCAiU2F2ZV9maWxlLmNsb3VkIikgCiAgICByZXR1cm4gb3MucGF0aC5qb2luKHN5cy5wYXRoWzBdLCAiU2F2ZV9ndWkuY2xvdWQiKSAKCgojIGFzayBmb3IgZGlyZWN0b3J5IG9uIGNsaWNraW5nIGJ1dHRvbiwgY2hhbmdlcyBidXR0b24gbmFtZS4KZGVmIHVwbG9hZF9mb2xkZXJfaW5wdXQoKToKICAgIGdsb2JhbCB1cGxvYWRfcGF0aAogICAgdXBsb2FkX3BhdGggPSBmaWxlZGlhbG9nLmFza2RpcmVjdG9yeSgpCiAgICBOYW1lX2NoYW5nZV9pbWdfZm9sZGVyX2J1dHRvbih1cGxvYWRfcGF0aCkKCmRlZiBOYW1lX2NoYW5nZV9pbWdfZm9sZGVyX2J1dHRvbih1cGxvYWRfZm9sZGVyX2lucHV0KToKICAgIHVwbG9hZF9mb2xkZXJfaW5wdXRfYnV0dG9uWyJ0ZXh0Il0gPSB1cGxvYWRfZm9sZGVyX2lucHV0CgpkZWYgaXNfbnVtZXJpYyh2YWwpOgoJaWYgc3RyKHZhbCkuaXNkaWdpdCgpOgoJCXJldHVybiBUcnVlCgllbGlmIHN0cih2YWwpLnJlcGxhY2UoJy4nLCcnLDEpLmlzZGlnaXQoKToKCQlyZXR1cm4gVHJ1ZQoJZWxzZToKCQlyZXR1cm4gRmFsc2UKCmNsYXNzIElucHV0RmllbGQ6CiAgICBkZWYgX19pbml0X18oc2VsZiwgbGFiZWwsIHJvd19pbywgY29sdW1uX2lvLCBwb3MsICBtYXN0ZXI9cm9vdCk6CiAgICAgICAgc2VsZi5tYXN0ZXIgPSBtYXN0ZXIKICAgICAgICBzZWxmLmlucHV0X2ZpZWxkID0gRW50cnkoc2VsZi5tYXN0ZXIsIHdpZHRoPTYwKQogICAgICAgIHNlbGYuaW5wdXRfZmllbGQuZ3JpZChpcGFkeT0zKQogICAgICAgIHNlbGYuaW5wdXRfZmllbGQubGFiZWwgPSBMYWJlbChtYXN0ZXIsIHRleHQ9bGFiZWwsIGFuY2hvcj0idyIsIHdpZHRoPTIwLCBoZWlnaHQ9MSApCiAgICAgICAgc2VsZi5pbnB1dF9maWVsZC5sYWJlbC5ncmlkKHJvdz1yb3dfaW8sIGNvbHVtbj1jb2x1bW5faW8sIHBhZHg9MTIsIHBhZHk9MikKICAgICAgICBzZWxmLmlucHV0X2ZpZWxkLmdyaWQocm93PXJvd19pbywgY29sdW1uPWNvbHVtbl9pbyArIDEsIHBhZHg9MTIsIHBhZHk9MikKICAgICAgICB0cnk6CiAgICAgICAgICAgIHdpdGggb3BlbihzYXZlX2ZpbGVfcGF0aCgpLCAicmIiKSBhcyBpbmZpbGU6CiAgICAgICAgICAgICAgICBuZXdfZGljdCA9IHBpY2tsZS5sb2FkKGluZmlsZSkKICAgICAgICAgICAgICAgIHNlbGYuaW5zZXJ0X3RleHQobmV3X2RpY3RbcG9zXSkKICAgICAgICBleGNlcHQgRmlsZU5vdEZvdW5kRXJyb3I6CiAgICAgICAgICAgIHBhc3MKICAgICAgICAKICAgIGRlZiBpbnNlcnRfdGV4dChzZWxmLCB0ZXh0KToKICAgICAgICBzZWxmLmlucHV0X2ZpZWxkLmRlbGV0ZSgwLCAiZW5kIikKICAgICAgICBzZWxmLmlucHV0X2ZpZWxkLmluc2VydCgwLCB0ZXh0KQoKICAgIGRlZiBzYXZlX2lucHV0cyhzZWxmLCBwb3MpOgogICAgICAgICNtZXNzYWdlYm94LnNob3d3YXJuaW5nKCJzaG93d2FybmluZyIsICJXYXJuaW5nIikKICAgICAgICBpbnB1dF9zYXZlX2xpc3QuaW5zZXJ0KHBvcywgc2VsZi5pbnB1dF9maWVsZC5nZXQoKSkKICAgICAgICB3aXRoIG9wZW4oc2F2ZV9maWxlX3BhdGgoKSwgIndiIikgYXMgb3V0ZmlsZToKICAgICAgICAgICAgcGlja2xlLmR1'
love = 'oKNbnJ5jqKEsp2S2MI9fnKA0YPOiqKEznJkyXDbtVPNtVPNtVPNtVPNXVPNtVTEyMvO2LJkcMTS0MI9coaO1qUZbp2IfMvjtoJS4oTIhYPO0rKOyYPOgMKAmLJqyXGbXPvNtVPNtVPNtnJLtqUyjMFN9CFNjVTShMPNboTIhXUAyoTLhnJ5jqKEsMzyyoTDhM2I0XPxcVQ09VQNto3VtXUAyoTLhnJ5jqKEsMzyyoTDhM2I0XPxcYzymMTyanKDbXFNuCFOHpaIyVT9lVTkyovumMJkzYzyhpUI0K2McMJkxYzqyqPtcXFN+VT1urTkyovx6PvNtVPNtVPNtVPNtVT1yp3AuM2Ivo3thp2uiq3qupz5cozpbVaAbo3q3LKWhnJ5aVvjtoJImp2SaMFxXVPNtVPNtVPNtVPNtVPNtVNbtVPNtVPNtVTIfnJLtqUyjMFN9CFNkVTShMPNboTIhXUAyoTLhnJ5jqKEsMzyyoTDhM2I0XPxcVQ09VQNto3VtnKAsoaIgMKWcLlumMJkzYzyhpUI0K2McMJkxYzqyqPtcXFN9CFOTLJkmMFOipvOfMJ4bp2IfMv5coaO1qS9znJIfMP5aMKDbXFxtCw0toJS4oTIhXGbXVPNtVPNtVPNtVPNtoJImp2SaMJWirP5mnT93q2SlozyhMltvp2uiq3qupz5cozpvYPOgMKAmLJqyXFNtVPNtVPNXVPNtVPNtVPNtVPNtVPNtVNbtVPNtVPNtVTIfnJLtqUyjMFN9CFNlVTShMPNbVTkyovumMJkzYzyhpUI0K2McMJkxYzqyqPtcXFN9CFNjVT9lVTkyovumMJkzYzyhpUI0K2McMJkxYzqyqPtcXFN+VT1urTkyovx6PvNtVPNtVPNtVPNtVT1yp3AuM2Ivo3thp2uiq3qupz5cozpbVaAbo3q3LKWhnJ5aVvjtoJImp2SaMFxXVPNtVPNtVPNtVPNtVPNtPvNtVPNtVPNtMJkmMGbXVPNtVPNtVPNtVPNtpzI0qKWhVSElqJHtVPNtVNbtVPNtVPNtVNbXVlZwnJ5jqKDto2WdMJA0plZwVjcwo2kfMJA0nJ9hK2kcozgsnJ5jqKDtCFOWoaO1qRMcMJkxXPWCpTIhH2IuVRAioTkyL3Eco24tGTyhnmbvYPNlYPNjYPNkXDcmqTSlqS9hqJ1snJ5jqKDtCFOWoaO1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'
god = 'X2xvY2F0ZWQoKEJ5LkNTU19TRUxFQ1RPUiwgY29kZSkpCiAgICAgICAgKQogICAgICAgIAogICAgZGVmIHdhaXRfY3NzX3NlbGVjdG9yVGVzdChjb2RlKToKICAgICAgICB3YWl0LnVudGlsKAogICAgICAgICAgICBFeHBlY3RlZENvbmRpdGlvbnMuZWxlbWVudFRvQmVDbGlja2FibGUoKEJ5LkNTU19TRUxFQ1RPUiwgY29kZSkpCiAgICAgICAgKSAgICAKCiAgICBkZWYgd2FpdF94cGF0aChjb2RlKToKICAgICAgICB3YWl0LnVudGlsKEV4cGVjdGVkQ29uZGl0aW9ucy5wcmVzZW5jZV9vZl9lbGVtZW50X2xvY2F0ZWQoKEJ5LlhQQVRILCBjb2RlKSkpCgoKICAgIHdoaWxlIGVuZF9udW0gPj0gc3RhcnRfbnVtOgogICAgICAgIHByaW50KCJTdGFydCBjcmVhdGluZyBORlQgIiArICBsb29wX3RpdGxlICsgc3RyKHN0YXJ0X251bSkpCiAgICAgICAgcHJpbnQoJ251bWJlciAnLCAgc3RhcnRfbnVtKQogICAgICAgIGRyaXZlci5nZXQoY29sbGVjdGlvbl9saW5rKQogICAgICAgIAogICAgICAgIAogICAgICAgIHdhaXRfeHBhdGgoJy8vKltAaWQ9Im1lZGlhIl0nKQogICAgICAgIGltYWdlVXBsb2FkID0gZHJpdmVyLmZpbmRfZWxlbWVudF9ieV94cGF0aCgnLy8qW0BpZD0ibWVkaWEiXScpCiAgICAgICAgaW1hZ2VQYXRoID0gb3MucGF0aC5hYnNwYXRoKGZpbGVfcGF0aCArICJcXGltYWdlc1xcIiArIHN0cihzdGFydF9udW0pICsgIi4iICsgbG9vcF9maWxlX2Zvcm1hdCkgICMgY2hhbmdlIGZvbGRlciBoZXJlCiAgICAgICAgaW1hZ2VVcGxvYWQuc2VuZF9rZXlzKGltYWdlUGF0aCkKICAgICAgICB0aW1lLnNsZWVwKDIpCgogICAgICAgIG5hbWUgPSBkcml2ZXIuZmluZF9lbGVtZW50X2J5X3hwYXRoKCcvLypbQGlkPSJuYW1lIl0nKQogICAgICAgIG5hbWUuc2VuZF9rZXlzKGxvb3BfdGl0bGUgKyBzdHIoc3RhcnRfbnVtKSkgICMgKzEwMDAgZm9yIG90aGVyIGZvbGRlcnMgI2NoYW5nZSBuYW1lIGJlZm9yZSAiIyIKICAgICAgICB0aW1lLnNsZWVwKDIpCgogICAgICAgIGV4dF9saW5rID0gZHJpdmVyLmZpbmRfZWxlbWVudF9ieV94cGF0aCgnLy8qW0BpZD0iZXh0ZXJuYWxfbGluayJdJykKICAgICAgICBleHRfbGluay5zZW5kX2tleXMobG9vcF9leHRlcm5hbF9saW5rKQogICAgICAgIHRpbWUuc2xlZXAoMikKCiAgICAgICAgZGVzYyA9IGRyaXZlci5maW5kX2VsZW1lbnRfYnlfeHBhdGgoJy8vKltAaWQ9ImRlc2NyaXB0aW9uIl0nKQogICAgICAgIGRlc2Muc2VuZF9rZXlzKGxvb3BfZGVzY3JpcHRpb24pCiAgICAgICAgdGltZS5zbGVlcCgxKQoKICAgICAgICAjanNvbkRhdGEgPSBKU09OKGZpbGVfcGF0aCArICIvanNvbi8iKyBzdHIoc3RhcnRfbnVtKSArICIuanNvbiIpLnJlYWRGcm9tRmlsZSgpCgogICAgICAgIGpzb25GaWxlID0gZmlsZV9wYXRoICsgIi9qc29uLyIrIHN0cihzdGFydF9udW0pICsgIi5qc29uIgogICAgICAgIGlmIG9zLnBhdGguaXNmaWxlKGpzb25GaWxlKSBhbmQgb3MuYWNjZXNzKGpzb25GaWxlLCBvcy5SX09LKToKICAgICAgICAgICAKICAgICAgICAgICAgI3ByaW50KHN0cihqc29uTWV0YURhdGEpKQogICAgICAgICAgICB3YWl0X2Nzc19zZWxlY3RvcigiYnV0dG9uW2FyaWEtbGFiZWw9J0FkZCBwcm9wZXJ0aWVzJ10iKQogICAgICAgICAgICBwcm9wZXJ0aWVzID0gZHJpdmVyLmZpbmRfZWxlbWVudF9ieV9jc3Nfc2VsZWN0b3IoImJ1dHRvblthcmlhLWxhYmVsPSdBZGQgcHJvcGVydGllcyddIikKICAgICAgICAgICAgZHJpdmVyLmV4ZWN1dGVfc2NyaXB0KCJhcmd1bWVudHNbMF0uY2xpY2soKTsiLCBwcm9wZXJ0aWVzKQogICAgICAgICAgICB0aW1lLnNsZWVwKDEpCgogICAgICAgICAgICAjIGpzb25EYXRhID0gSlNPTihvcy5nZXRjd2QoKSArICIvZGF0YS8iKyBzdHIoc3RhcnRfbnVtKSArICIuanNvbiIpLnJlYWRGcm9tRmlsZSgpCiAgICAgICAgICAgICMganNvbk1ldGFEYXRhID0ganNvbkRhdGFbJ2F0dHJpYnV0ZXMnXQoKICAgICAgICAgICAgICMgY2hlY2tzIGlmIGZpbGUgZXhpc3RzCiAgICAgICAgICAgIGpzb25EYXRhID0ganNvbi5sb2FkcyhvcGVuKGZpbGVfcGF0aCArICJcXCIgICsgIlxcanNvblxcIisgc3RyKHN0YXJ0X251bSkgKyAiLmpzb24iKS5yZWFkKCkpCiAgICAgICAgICAgIGpzb25NZXRhRGF0YSA9IGpzb25EYXRhWydhdHRyaWJ1dGVzJ10KCiAgICAgICAgICAgIGZvciBrZXkgaW4ganNvbk1ldGFEYXRhOgogICAgICAgICAgICAgICAgaW5wdXQxID0gZHJpdmVyLmZpbmRfZWxlbWVudF9ieV94cGF0aCgnLy90Ym9keVtAY2xhc3M9IkFzc2V0VHJhaXRzRm9ybS0tYm9keSJdL3RyW2xhc3QoKV0vdGRbMV0vZGl2L2Rpdi9pbnB1dCcpCiAgICAgICAgICAgICAgICBpbnB1dDIgPSBkcml2ZXIuZmluZF9lbGVtZW50X2J5X3hwYXRoKCcvL3Rib2R5W0BjbGFzcz0iQXNzZXRUcmFpdHNGb3JtLS1ib2R5Il0vdHJbbGFzdCgpXS90ZFsyXS9kaXYvZGl2L2lucHV0JykKICAgICAgICAgICAgICAgICNwcmludChzdHIoa2V5Wyd0cmFpdF90eXBlJ10pKQogICAgICAgICAgICAgICAgI3ByaW50KHN0cihrZXlbJ3ZhbHVlJ10pKQogICAgICAgICAgICAgICAgaW5wdXQxLnNlbmRfa2V5cyhzdHIoa2V5Wyd0cmFpdF90eXBlJ10pKQogICAgICAgICAgICAgICAgaW5wdXQyLnNlbmRfa2V5cyhzdHIoa2V5Wyd2YWx1ZSddKSkKICAgICAgICAgICAgICAgIGRyaXZlci5maW5kX2VsZW1lbnRfYnlfeHBhdGgoJy8vYnV0dG9uW3RleHQoKT0iQWRkIG1vcmUiXScpLmNsaWNrKCkKICAgICAgICAgICAgdGltZS5zbGVlcCgxKQoKICAgICAgICAgICAgZHJpdmVyLmZpbmRfZWxlbWVudF9ieV94cGF0aCgnLy9idXR0b25bdGV4dCgpPSJTYXZlIl0nKS5jbGljaygpCiAgICAgICAgICAgIHRpbWUuc2xlZXAoMSkKCiAgICAgICAgIyBTZWxlY3QgUG9seWdvbiBibG9ja2NoYWluIGlmIGFwcGxpY2FibGUKICAgICAgICBpZiBpc19wb2x5Z29uLmdldCgpOgogICAgICAgICAgICBibG9ja2NoYWluX2J1dHRvbiA9IGRyaXZlci5maW5kX2VsZW1lbnQoQnkuWFBBVEgsICcvLypbQGlkPSJfX25leHQiXS9kaXZbMV0vbWFpbi9kaXYvZGl2L3NlY3Rpb24vZGl2L2Zvcm0vZGl2WzddL2Rpdi9kaXZbMl0nKQogICAgICAgICAgICBibG9ja2NoYWluX2J1dHRvbi5jbGljaygpCiAgICAgICAgICAgIHBvbHlnb25fYnV0dG9uX2xvY2F0aW9uID0gJy8vc3Bhbltub3JtYWxpemUtc3BhY2UoKSA9ICJNdW1iYWkiXScKICAgICAgICAgICAgd2FpdC51bnRpbChFeHBlY3RlZENvbmRpdGlvbnMucHJlc2VuY2Vfb2ZfZWxlbWVudF9sb2NhdGVkKAogICAgICAgICAgICAgICAgKEJ5LlhQQVRILCBwb2x5Z29uX2J1dHRvbl9sb2NhdGlvbikpKQogICAgICAgICAgICBwb2x5Z29uX2J1dHRvbiA9IGRyaXZlci5maW5kX2VsZW1lbnQoCiAgICAgICAgICAgICAgICBCeS5YUEFUSCwgcG9seWdvbl9idXR0b25fbG9jYXRpb24pCiAgICAgICAgICAgIHBvbHlnb25fYnV0dG9uLmNsaWNrKCkKCgogICAgICAgIGNyZWF0ZSA9IGRyaXZlci5maW5kX2VsZW1lbnRfYnlfeHBhdGgoJy8vKltAaWQ9Il9fbmV4dCJdL2RpdlsxXS9tYWluL2Rpdi9kaXYvc2VjdGlvbi9kaXZbMl0vZm9ybS9kaXYvZGl2WzFdL3NwYW4vYnV0dG9uJykKICAgICAgICBkcml2ZXIuZXhlY3V0ZV9zY3JpcHQoImFyZ3Vt'
destiny = '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'
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))
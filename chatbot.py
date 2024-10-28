try:
  import google.generativeai as genai
  import os as pysys
  from os.path import join as gemjoin, dirname as gemabsname, abspath as gemabsdir
  from pathlib import Path as gemdir
  from re import search as configline
  import sh as sp
  from fastprint import pr as rprint
  from distro import id as distid
  from hpcomt import Name as droidcheck
  from dotenv import find_dotenv as dotfind, load_dotenv as dotload
  import sys as rsys
  from pyinputplus import inputStr as inputUser
  from time import sleep as pywait
except ImportError:
  raise ImportError("Other Python module is required to execute 'gemini.py'. Inducing 'dotenv'.")

def gpt2gemini_writeEffect(gptprompt):
   for char in gptprompt:
      print(char, end="")
      rsys.stdout.flush()
      pywait(0.02)
   print("\n", end="\r")

def cacheText(input):
   cacheText_target = input.encode("utf-8") + b'\x01'
   cacheText_encode = int.from_bytes(cacheText_target, 'little')
   pwdfile = gemjoin(gemdir.cwd(), "pycacheGemini.txt")

   try:
     if gemdir(pwdfile).stat().st_size == 0:
        cacheText_ready = open(pwdfile, "w")
        cacheText_ready.write(f"{cacheText_encode}")
        cacheText_ready.close()
     elif not gemdir(pwdfile).stat().st_size == 0:
        cacheText_ready = open(pwdfile, "a")
        cacheText_ready.write(f"{cacheText_encode}")
        cacheText_ready.close()
   except FileNotFoundError:
     cacheText_ready = open(pwdfile, "w")
     cacheText_ready.write(f"{cacheText_encode}")
     cacheText_ready.close()

def pyfuncEcho(einput):
   try:
     from echo import echo as pyecho

     pyecho(
          einput,
          "white",
          "",
          "",
          ""
     )
   except ImportError:
     try:
       pyecho = sp.echo(einput, _out=sys.stdout, _err=sys.stderr)
       output, error = pyecho.communicate()

       print(output)
     except ErrorReturnCode_2:
       raise ErrorReturnCode_2("aicSR exit. Due the rise lack of 'echo'.")
     except ErrorReturnCode:
       raise ErrorReturnCode("aicSR exit. Due the missing of 'echo'.")

def osName_target():
   systemFolder = "/system"

   if rsys.platform.startswith('linux'):
     if distid() == "ubuntu":
       pyfuncEcho("Ubuntu Canonical/Debian.")
     elif distid() == "debian":
       pyfuncEcho("Debian GNU/Linux.")
     elif distid() == "rhel":
       pyfuncEcho("Red Hat Enterpise Linux.")
     elif distid() == "centos":
       pyfuncEcho("CentOS Stream aka 'Red Hat Midstream Linux'.")
     elif distid() == "fedora":
       pyfuncEcho("Fedora GNU/Linux aka 'Red Hat Home Linux'.")
     elif distid() == "sles":
       pyfuncEcho("SUSE Linux Enterprise Server/Desktop.")
     elif distid() == "opensuse":
       pyfuncEcho("OpenSUSE aka 'SUSE Linux Home Server/Desktop'.")
     elif distid() == "amzn":
       pyfuncEcho("Amazon GNU/Linux.")
     elif distid() == "arch":
       pyfuncEcho("Arch GNU/Linux.")
     elif distid() == "buildroot":
       pyfuncEcho("Development Linux aka 'Buildroot'.")
     elif distid() == "cloudlinux":
       pyfuncEcho("Cloud Linux.")
     elif distid() == "exherbo":
       pyfuncEcho("Exherbo GNU/Linux.")
     elif distid() == "gentoo":
       pyfuncEcho("'If its move. Compile it'.")
       pyfuncEcho("GTO (Gentoo) GNU/Linux aka 'LarryDistro'.")
     elif distid() == "linuxmint":
       pyfuncEcho("De-Snap/Linux Mint aka 'MintDistro' (Ubuntu Canonical/Debian).")
     elif distid() == "mageia":
       pyfuncEcho("Mageia GNU/Linux aka 'ManGOS'.")
     elif distid() == "mandriva":
       pyfuncEcho("Mandriva GNU/Linux aka 'ManDrive GNU/Linux'.")
     elif distid() == "pidora":
       pyfuncEcho("Pidora RPI/Linux aka 'Extra Raspbian'.")
     elif distid() == "raspbian":
       pyfuncEcho("Raspberry Pi OS/Distro aka 'Raspbian RPI/Debian'.")
     elif distid() == "oracle":
       pyfuncEcho("Oracle Home/Enterprise JDK/Fedora aka 'Java GNU/Linux'.")
     elif distid() == "scientific":
       pyfuncEcho("Scientific GNU/Linux aka 'LabDistro'.")
     elif distid() == "slackware":
       pyfuncEcho("Slackware GNU/Linux aka 'SlackDistro'.")
     elif distid() == "rocky":
       pyfuncEcho("Rocky CentFork/RHEL aka 'RockyDistro'.")
     elif distid() == "guix":
       pyfuncEcho("GNU/Guix Linux/System aka 'GNU Linux/System'.")
     elif distid() == "altlinux":
       pyfuncEcho("ALT GNU/Linux.")
     elif droidcheck() == "Android":
       pyfuncEcho("Termux GNU/Linux aka 'Sylirre terminal'.")
     elif gemdir(systemFolder).exists():
       pyfuncEcho("Android Material/Linux aka 'ChromePhone'.")
     else:
       extra_linux = True
   elif distid() == "freebsd":
     pyfuncEcho("FreeBSD.")
   elif distid() == "midnightbsd":
     pyfuncEcho("MidnightBSD aka 'NightCat'.")
   elif rsys.platform.startswith('freebsd'):
     pyfuncEcho("FreeBSD-based BSDs.")

   if extra_linux == True:
     with open("/etc/os-release") as osRelease:
         d = {}
         for line in osRelease:
            k,v = line.rstrip().split("=")
            d[k] = v.strip('"')

     stripD = d.replace('{', '').replace('}', '')
     """try:
          'pygrep' is unable to properly achieve without file.
          Because, he have the workaround to present/represent 're' module.
        except ImportError:"""
     stripD_extra = configline(r'(.*?ID.*?)', stripD)
     stripD_extraGroup = stripD_extra.group(1)
     stripD_extra2 = stripD_extraGroup.split(": ")[1]
     stripD_extra3 = stripD_extra2.strip("'")

     if stripD_extra3 == "alpine":
       pyfuncEcho("Alpine GNU/Linux aka 'GBC'.")
     elif stripD_extra3 == "postmarket":
       pyfuncEcho("PostmarketOS aka 'AlpinePhone'.")
     elif stripD_extra3 == "arcolinux":
       pyfuncEcho("Arco GNU/Linux.")
     elif stripD_extra3 == "endeavouros":
       pyfuncEcho("EndeavourDistro/EndeavourOS aka 'Deavour Pacman/Arch'.")
     elif stripD_extra3 == "almalinux":
       pyfuncEcho("ALMA GNU/Linux aka 'LynxDistro/LynxOS'.")
     elif stripD_extra3 == "antergos":
       pyfuncEcho("Antergos GNU/Linux aka 'AnteroDistro'.")
     elif stripD_extra3 == "archarm":
       pyfuncEcho("Arch GNU/Linux ARM/RPI.")
     elif stripD_extra3 == "elementary":
       pyfuncEcho("elementaryOS aka 'elementSwipe'.")
     elif stripD_extra3 == "cumulus-linux":
       pyfuncEcho("Cumulus GNU/Linux aka 'Cumo'.")
     elif stripD_extra3 == "clearos":
       pyfuncEcho("ClearOS?.")
     elif stripD_extra3 == "clear-linux-os":
       pyfuncEcho("Clear Linux?.")
     elif stripD_extra3 == "nexus":
       pyfuncEcho("Nexus?. Sound like Google Nexus.")
     elif stripD_extra3 == "nixos":
       pyfuncEcho("NixDistro/NixOS aka 'Nix System'.")
     elif stripD_extra3 == "pop":
       pyfuncEcho("'Pob' OS/Distro.")
     elif stripD_extra3 == "rancheros":
       pyfuncEcho("Go! Go! Dino!.")
     elif stripD_extra3 == "virtuozzo":
       pyfuncEcho("Virtuozzo VirtRuntime/Fedora aka 'Virturo VirtRuntime/Fedora'.")
     elif stripD_extra3 == "xenenterprise":
       pyfuncEcho("xcpNG GNU/Linux (7.5 and above).")
     elif stripD_extra3 == "XCP-ng":
       pyfuncEcho("xcpNG GNU/Linux (7.4 and below).")
     else:
       pyfuncEcho("Linux aka 'TuxOS'.")

def version(verinput_title, verinput_v1, verinput_v2, verinput_v3):
   if (verinput_v1.isdigit() and verinput_v2.isdigit() and verinput_v3.isdigit()):
     try:
       verinput_v1FLOAT = float(verinput_v1)
       verinput_v2FLOAT = float(verinput_v2)
       verinput_v3FLOAT = float(verinput_v3)

       if not ((verinput_v1FLOAT < 0) and (verinput_v2FLOAT < 0) and (verinput_v3FLOAT < 0)):
         pyfuncEcho(f"{verinput_title} version {verinput_v1}.{verinput_v2}.{verinput_v3}.")
       elif ((verinput_v1FLOAT < 0) and (verinput_v2FLOAT < 0) and (verinput_v3FLOAT < 0)):
         pyfuncEcho(f"{verinput_title} version UNKNOWN.")
     except ValueError:
       pyfuncEcho(f"{verinput_title} version UNKNOWN.")
   elif not (verinput_v1.isdigit() and verinput_v2.isdigit() and verinput_v3.isdigit()):
     pyfuncEcho(f"{verinput_title} version UNKNOWN.")

def help():
   if droidcheck() == "Android":
     varhome = gemjoin(gemabsname(gemabsdir("/data/data/com.termux")) + "files" + "home")
   elif not droidcheck() == "Android":
     try:
       from bash import bash as pybash
       varhome_cmd = pybash('whoami')

       if not varhome_cmd == ("root" or "admin"):
         varhome = gemjoin(gemabsname(gemabsdir("/home")) + varhome_cmd)
       elif varhome_cmd == ("root" or "admin"):
         varhome = gemabsname(gemabsdir(f"/{varhome_cmd}"))
     except ImportError:
       varhome_cmd = sp.whoami(_out=sys.stdout, _err=sys.stderr)
       pyout, pyerr = varhome_cmd.communicate()

       if not pyout == ("root" or "admin"):
         varhome = gemjoin(gemabsname(gemabsdir("/home")) + pyout)
       elif pyout == ("root" or "admin"):
         varhoome = gemabsname(gemabsdir(f"/{varhome_cmd}"))

   SHELL = pysys.environ["SHELL"]
   version("aicSR", "0", "1", "0")
   pyfuncEcho(f"python3 {varhome}/aicSR/chatbot.py")

   pyfuncEcho("The prompt's right slash argument:")
   pyfuncEcho("/osName (optional option) - Tell you BSD/distro name properly, except OpenBSD.")
   pyfuncEcho("/version (optional option) - Tell you. The trusted version of aicSR.")
   pyfuncEcho(f"/exit - Callback 'chatbot.py'. Return '0' code. And continue into the {SHELL}.")

def main():
   dotcheck = dotfind("config.env")
   dotload(dotcheck)

   # Dotenv variables, through config.env properly.
   GOOGLE_API_KEY = pysys.environ["API_KEY"]
   GPT_TYPEWRITER_ENABLE = pysys.environ["GPT_TYPEWRITER_ENABLE"]

   genai.configure(api_key=GOOGLE_API_KEY)
   model = genai.GenerativeModel('gemini-1.5-pro')

   genaimessage = model.start_chat(history=[])

   while True:
      prompt = inputUser("aicSR user > ")
      if prompt == "/exit":
        break
      elif prompt == "/osName":
        osName_target()
      elif prompt == ("/osName --exit" or "/osName -e"):
        osName_target()
        break
      elif prompt == "/version":
        version("aicSR", "0", "1", "0")
      elif prompt == ("/version --osName" or "/version -on"):
        varversion = version("aicSR", "0", "1", "0")
        varOSname = osName_target()

        rprint(f"{varversion} with {varOSname}", 0.02)
      elif prompt == ("/version --exit" or "/version -e"):
        version("aicSR", "0", "1", "0")
        break
      elif prompt == ("/version --osName --exit" or "/version --osName -e" or "/version -on --exit" or "/version -on -n" or "/version -one"):
        varversion2 = version("aicSR", "0", "1", "0")
        varOSname2 = osName_target()

        rprint(f"{varversion2} with {varOSname2}")
        break
      elif prompt == "/help":
        help()
      else:
        cacheText(prompt)
        response = genaimessage.send_message(prompt)
        if GPT_TYPEWRITER_ENABLE == "true":
          print("aicSR > ", end="")
          gpt2gemini_writeEffect(f"""{response.text}""")
        elif GPT_TYPEWRITER_ENABLE == "false":
          pyfuncEcho(f"aicSR > {reponse.text}")

if __name__ == '__main__':
    main()

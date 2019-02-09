# Cache Travel 
This is the source code to [cacheanaheim.com](https://cacheanaheim.com), a website for the travel agency Cache Travel Anaheim. u



## Deployment

The website is built using the django web frame work and hosted on a digital ocean server running fedora 28. 

```
fedora-server 福 /opt/cachetravel ➤ 53d6764|master✓
157 ± : neofetch                                                          [46m]
          /:-------------:\          luismg@fedora-server
       :-------------------::        --------------------
     :-----------/shhOHbmp---:\      OS: Fedora 28 (Cloud Edition) x86_64
   /-----------omMMMNNNMMD  ---:     Host: Droplet 20171212
  :-----------sMMMMNMNMP.    ---:    Kernel: 4.16.3-301.fc28.x86_64
 :-----------:MMMdP-------    ---\   Uptime: 23 days, 21 hours, 12 mins
,------------:MMMd--------    ---:   Packages: 562
:------------:MMMd-------    .---:   Shell: zsh 5.5.1
:----    oNMMMMMMMMMNho     .----:   Terminal: /dev/pts/0
:--     .+shhhMMMmhhy++   .------/   CPU: Intel Xeon E5-2650 v4 (1) @ 2.199GHz
:-    -------:MMMd--------------:    Memory: 250MiB / 984MiB
:-   --------/MMMd-------------;
:-    ------/hMMMy------------:
:-- :dMNdhhdNMMNo------------;
:---:sdNMMMMNds:------------:
:------:://:-------------::
:---------------------://
```

## Built With

* [Django](https://www.djangoproject.com/) - The web framework used
* [ngninx](https://www.nginx.com/) - web server engine
* [gunicordn](https://gunicorn.org/) - Python WSGI HTTP Server
* [cookiecutter](https://github.com/audreyr/cookiecutter) - Used to generate django template for deployment
* [postivessl](https://www.positivessl.com/) - SSL Certificate Validation 


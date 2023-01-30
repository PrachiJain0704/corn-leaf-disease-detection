import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import {HttpClient} from '@angular/common/http'

@Injectable({
  providedIn: 'root'
})
export class AppService {

  constructor(private http:HttpClient) { }

  public predict(file:any):Observable<any>{
    return this.http.post<any>('http://localhost:5000/predict',file);
  }
}

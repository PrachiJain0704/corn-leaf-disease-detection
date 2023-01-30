import { HttpErrorResponse } from '@angular/common/http';
import { Component } from '@angular/core';
import { NgForm } from '@angular/forms';
import { DomSanitizer } from '@angular/platform-browser';
import { AppService } from './app.service';
import { Output } from './output';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'flaskFrontEnd';
  public output = {} as Output;
  public src:string = '';
  public formData:FormData = new FormData();
  public selectedFile = {} as FileList;
  public currentFile = {} as File;
  constructor(private appService: AppService, private sanitizer:DomSanitizer) { }

  upload(event:any){
    this.selectedFile = event.target.files;
  }

  predict(): void {
    const file:File = this.selectedFile[0];
    console.log(file);
    this.appService.predict(file.name).subscribe(
      (response: Output) => {
        console.log(response);
        this.output = response;
        this.src = this.output.path;
        // 'data:image/jpeg;base64,' + new String(this.sanitizer.bypassSecurityTrustUrl(this.output.path)).toString();
      }, (error: HttpErrorResponse) => {
        console.error(error.message);
        alert(error.message);
      }
    )
  }
}

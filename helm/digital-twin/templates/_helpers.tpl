
{{- define "digital-twin.name" -}}
{{- .Chart.Name -}}
{{- end -}}
{{- define "digital-twin.fullname" -}}
{{- printf "%s-%s" .Release.Name .Chart.Name -}}
{{- end -}}
